from project.celery import app
from celery.task.control import inspect
from logging import getLogger
from django.conf import settings

logger = getLogger(__name__)

if not settings.IS_TESTING:
    insp = inspect()
    if not insp.stats(): raise Exception('Workers not launched')


def apply_filter(resource_id, image_id, filter_type):
    if not settings.IS_TESTING:
        app.send_task('apply_filter', args=[resource_id, image_id, filter_type])
        logger.debug('Task sent')
    else:
        logger.warning('TEST task got')
