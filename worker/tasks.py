import base64
import os
from logging import getLogger
from tempfile import NamedTemporaryFile

from celery import Celery

from api_client import ApiClient
from base64_utils import clear_base64, convert_to_base64
from filters import FilterApplier

logger = getLogger(__name__)

app = Celery(
    'worker',
    broker=os.getenv('CELERY_BROKER_URL', 'amqp://localhost'),
    backend=os.getenv('CELERY_RESULT_BACKEND', 'amqp://localhost')
)


@app.task(name='apply_filter')
def apply_filter(resource_id, image_id, filter_type):
    logger.info('Got resource_id={resource_id}, image_id{image_id}, filter_type={filter_type}'.format(
        resource_id=resource_id, image_id=image_id, filter_type=filter_type
    ))
    api_client = ApiClient()
    temp_file = NamedTemporaryFile(delete=False, suffix='.png', mode='wb')

    base64_image = api_client.get_image_source(image_id)
    cleaned_base64_image = clear_base64(base64_image)

    png_source = base64.b64decode(cleaned_base64_image)
    temp_file.write(png_source)

    filter_applier = FilterApplier(temp_file.name, filter_type)
    filtered_file_name = filter_applier.apply_filter()

    logger.info('Saved filtered_file_name={filtered_file_name}'.format(
        filtered_file_name=filtered_file_name
    ))

    if filtered_file_name:
        filtered_base64_image = convert_to_base64(filtered_file_name)

        filtered_image_id = api_client.create_image(filtered_base64_image)

        api_client.update_resource_result(resource_id, filtered_image_id)

        return filtered_image_id
    return 'Error'
