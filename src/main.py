import supervisely_lib as sly

app: sly.AppService = sly.AppService()


@app.callback("create_foreground")
@sly.timeit
def create_foreground(api: sly.Api, task_id, context, state, app_logger):
    image_id = context["imageId"]
    threshold = state["threshold"]
    rewrite = state["rewrite"]
    pass


def main():
    data = {

    }
    state = {
        "threshold": 255,
        "rewrite": True,
        "classes": ""
    }
    app.run(data=data, state=state)


# @TODO: size: mini - sly-select-class
# @TODO: keep biggest connected component (ignore noise) VS keep all parts
# @TODO: add min instance version to config
if __name__ == "__main__":
    sly.main_wrapper("main", main)
