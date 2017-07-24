from project.celery import app
from celery.task.control import inspect


def apply_filter(resource_id, image_id, filter_type):
    insp = inspect()
    d = insp.stats()
    if d:
        app.send_task('apply_filter', args=[resource_id, image_id, filter_type])
        return True
    return False
