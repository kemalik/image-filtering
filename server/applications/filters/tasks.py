from project.celery import app
from celery.task.control import inspect
from logging import getLogger

logger = getLogger(__name__)


def is_workers_launched():
    insp = inspect()
    if not insp.stats():
        raise Exception('Workers not launched')


def apply_filter(resource_id, image_id, filter_type):
    is_workers_launched()
    app.send_task('apply_filter', args=[resource_id, image_id, filter_type])
    logger.debug('Task send')


is_workers_launched()
