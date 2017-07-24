import base64
import os
from logging import getLogger
from tempfile import NamedTemporaryFile

from celery import Celery

from api_client import ApiClient
from base64_utils import clear_base64, convert_to_base64
from filters import apply_edge_filter, apply_red_tint_filter, apply_swirl_filter

logger = getLogger(__name__)

app = Celery(
    'worker',
    broker=os.getenv('CELERY_BROKER_URL', 'amqp://localhost'),
    backend=os.getenv('CELERY_BROKER_URL', 'amqp://localhost')
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
    if filter_type == 'edge':
        filtered_file_name = apply_edge_filter(temp_file.name)
    elif filter_type == 'red_tint':
        filtered_file_name = apply_red_tint_filter(temp_file.name)
    elif filter_type == 'swirl':
        filtered_file_name = apply_swirl_filter(temp_file.name)
    else:
        filtered_file_name = None

    logger.info('Saved filtered_file_name={filtered_file_name}'.format(
        filtered_file_name=filtered_file_name
    ))

    if filtered_file_name:
        filtered_base64_image = convert_to_base64(filtered_file_name)

        filtered_image_id = api_client.create_image(filtered_base64_image)

        api_client.update_resource_result(resource_id, filtered_image_id)

        return filtered_image_id
    return 'Error'
