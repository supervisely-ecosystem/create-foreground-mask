import supervisely_lib as sly

app: sly.AppService = sly.AppService()


@app.callback("select_prev_object")
@sly.timeit
def prev_object(api: sly.Api, task_id, context, state, app_logger):
    pass


def main():
    data = {}
    state = {}
    app.run(data=data, state=state)


if __name__ == "__main__":
    sly.main_wrapper("main", main)
