import os
import numpy as np
import supervisely_lib as sly

app = sly.AppService()

team_id = int(os.environ['context.teamId'])
workspace_id = int(os.environ['context.workspaceId'])
project_id = int(os.environ["modal.state.slyProjectId"])

threshold = int(os.environ["modal.state.threshold"])
need_fuzzy = sly.env.flag_from_env(os.environ["modal.state.fuzzy"])

foreground = sly.ObjClass("foreground", sly.Bitmap, [0, 0, 255])
fuzzy = sly.ObjClass("fuzzy", sly.Bitmap, [128, 128, 128])

meta = None


def create_classes(api: sly.Api):
    def _check_and_add_class(meta: sly.ProjectMeta, target_class: sly.ObjClass):
        cls: sly.ObjClass = meta.get_obj_class(target_class.name)
        if cls is None:
            meta = meta.add_obj_class(target_class)
        elif cls != target_class:
            raise RuntimeError(f"Project already has class '{cls.name}' with shape {cls.geometry_type.geometry_name()}. "
                               f"Shape conflict: shape should be of typy {target_class.geometry_type.geometry_name()}")
        return meta

    global meta
    meta_json = api.project.get_meta(project_id)
    meta = sly.ProjectMeta.from_json(meta_json)

    meta_res = _check_and_add_class(meta, foreground)
    meta_res = _check_and_add_class(meta_res, fuzzy)

    if meta != meta_res:
        api.project.update_meta(project_id, meta_res.to_json())
    return meta_res


def get_masks(img):
    alpha = img[:, :, 3]
    mask_fg = alpha >= threshold
    mask_fuzzy = np.logical_and(alpha > 0, alpha < 255)

    fg = sly.Label(sly.Bitmap(mask_fg), foreground)
    fzz = None
    if np.any(mask_fuzzy) and need_fuzzy:
        fzz = sly.Label(sly.Bitmap(mask_fuzzy), fuzzy)

    return fg, fzz


@app.callback("create_foreground")
@sly.timeit
def create_foreground(api: sly.Api, task_id, context, state, app_logger):
    global meta
    project_info = api.project.get_info_by_id(project_id)
    meta = create_classes(api)

    progress = sly.Progress("Processing", project_info.items_count)
    for dataset in api.dataset.get_list(project_id):
        images_infos = api.image.get_list(dataset.id)
        for batch_infos in sly.batched(images_infos, 20):
            ids = []
            names = []
            local_paths = []
            for info in  batch_infos:
                ids.append(info.id)
                names.append(info.name)
                local_paths.append(os.path.join(app.data_dir, info.name))

            api.image.download_paths(dataset.id, ids, local_paths)
            anns_infos = api.annotation.download_batch(dataset.id, ids)
            anns = [sly.Annotation.from_json(info.annotation, meta) for info in anns_infos]

            res_ids = []
            res_anns = []
            for img_id, img_name, img_path, ann in zip(ids, names, local_paths, anns):
                img = sly.image.read(img_path, remove_alpha_channel=False)
                if len(img.shape) == 3:
                    if img.shape[2] != 4:
                        sly.logger.warn(f"Image {img_name} (id={img_id}) does not have alpha channel, will be skipped")
                        continue
                else:
                    sly.logger.warn(f"Image {img_name} (id={img_id}) does not have alpha channel, will be skipped")
                    continue

                fg, fuzzy = get_masks(img)

                new_ann = ann.add_label(fg)
                if fuzzy is not None:
                    new_ann = new_ann.add_label(fuzzy)

                res_ids.append(img_id)
                res_anns.append(new_ann)

            api.annotation.upload_anns(res_ids, res_anns)
            for img_path in local_paths:
                sly.fs.silent_remove(img_path)
            progress.iters_done_report(len(batch_infos))

    api.task.set_output_project(task_id, project_id)
    app.stop()


def main():
    sly.logger.info("Script arguments", extra={
        "TEAM_ID": team_id,
        "WORKSPACE_ID": workspace_id,
        "PROJECT_ID": project_id,
        "THRESHOLD": threshold,
        "NEED_FUZZY": need_fuzzy
    })
    app.run(initial_events=[{"command": "create_foreground"}])


if __name__ == "__main__":
    sly.main_wrapper("main", main)
