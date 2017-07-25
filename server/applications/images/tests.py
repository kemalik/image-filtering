from django.test import TestCase
from django.test import Client
import json

from applications.images.factories import ImageFactory
from applications.images.models import Image


class TestImagesApi(TestCase):
    def setUp(self):
        self.client = Client()
        super(TestImagesApi, self).setUp()

    def test_imges_url_returns_code_200(self):
        success_status = 200
        response = self.client.get('/api/images/')

        self.assertEqual(response.status_code, success_status)

    def test_imges_available_from_api_list(self):
        images_count = 10
        for i in range(images_count):
            ImageFactory()

        response = self.client.get('/api/images/')

        images = json.loads(response.content.decode('utf8'))
        self.assertEqual(len(images), images_count)

    def test_imges_available_from_detail_page(self):
        img = ImageFactory()

        response = self.client.get('/api/images/{id}/'.format(id=img.id))
        image = json.loads(response.content.decode('utf8'))
        self.assertEqual(image['image'], img.image().decode('utf8'))

    def test_delete_image_via_api(self):
        img = ImageFactory()

        self.client.delete('/api/images/{id}/'.format(id=img.id))

        self.assertFalse(Image.objects.all().exists())

    def test_can_create_image_via_api(self):
        self.client.post('/api/images/', data={'base64_image': 'data:image/png;base64,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'})

        self.assertTrue(Image.objects.exists())