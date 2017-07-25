import base64
import os
from logging import getLogger
from tempfile import NamedTemporaryFile

from celery import Celery

from helpers.api_client import ApiClient
from helpers.base64_utils import Base64Util
from helpers.filters import FilterApplier

logger = getLogger(__name__)

app = Celery(
    'worker',
    broker=os.getenv('CELERY_BROKER_URL', 'amqp://localhost'),
    backend=os.getenv('CELERY_RESULT_BACKEND', 'amqp://localhost')
)


@app.task(name='apply_filter')
def apply_filter(resource_id, image_id, filter_type):
    logger.info('Got resource_id={resource_id}, image_id={image_id}, filter_type={filter_type}'.format(
        resource_id=resource_id, image_id=image_id, filter_type=filter_type
    ))

    api_client = ApiClient()
    temp_file = NamedTemporaryFile(delete=False, suffix='.png', mode='wb')

    base64_image = api_client.get_image_source(image_id)

    base64_util = Base64Util(base64_image)
    png_source = base64_util.decode_base64()

    temp_file.write(png_source)

    filter_applier = FilterApplier(temp_file.name, filter_type)
    filtered_file_name = filter_applier.apply_filter()

    if filtered_file_name:
        logger.info('Saved filtered_file_name = {filtered_file_name}'.format(
            filtered_file_name=filtered_file_name
        ))

        filtered_base64_image = base64_util.convert_image_to_base64(filtered_file_name)

        filtered_image_id = api_client.create_image(filtered_base64_image)

        api_client.update_resource_result(resource_id, filtered_image_id)

        return filtered_image_id

    logger.error('Error while apply filter')
    return 'error'
