from project.celery import app


def apply_filter(image_id, filter_type):
    app.send_task('apply_filter', args=[image_id, filter_type])
