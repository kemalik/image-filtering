import requests


class ApiClient(object):
    def __init__(self) -> None:
        self.url = 'http://localhost:8000/'

    def get_image_source(self, image_id):
        pass

    def create_image(self, source):
        pass

    def update_rource_result(self, source_id, image_id):
        pass
