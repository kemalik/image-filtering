from project.celery import app


def apply_filter(resource_id, image_id, filter_type):
    app.send_task('apply_filter', args=[resource_id, image_id, filter_type])
