import os
from logging import getLogger
from urllib import parse

import requests

logger = getLogger(__name__)


class ApiClient(object):
    def __init__(self) -> None:
        self.url = os.getenv('SERVER_HOST', 'http://localhost:8000/')

    def get_image_source(self, image_id):
        get_image_url = parse.urljoin(self.url, '/api/images/{image_id}/'.format(image_id=image_id))

        response = requests.get(get_image_url)
        if response.status_code == 200:
            return response.json()['image']
        return ''

    def create_image(self, source):
        create_image_url = parse.urljoin(self.url, '/api/images/')

        response = requests.post(create_image_url, data={'base64_image': source})
        if response.status_code == 201:
            return response.json()['id']
        return ''

    def update_resource_result(self, source_id, image_id):
        update_source_url = parse.urljoin(self.url, '/api/filter/{source_id}/'.format(source_id=source_id))

        response = requests.patch(update_source_url, data={'result': image_id, 'status': 'done'})
        return response.status_code == 200
