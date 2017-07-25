from django.test import TestCase
from django.test import Client
import json

from applications.filters.factories import FilteredResourceFactory
from applications.filters.models import FilteredResource
from applications.images.factories import ImageFactory


class FilteredResourceFactoryApi(TestCase):
    def setUp(self):
        self.client = Client()
        super(FilteredResourceFactoryApi, self).setUp()

    def test_filter_url_returns_code_200(self):
        success_status = 200
        response = self.client.get('/api/filter/')

        self.assertEqual(response.status_code, success_status)

    def test_resources_available_from_api_list(self):
        resources_count = 10
        for i in range(resources_count):
            FilteredResourceFactory()

        response = self.client.get('/api/filter/')

        resources = json.loads(response.content.decode('utf8'))
        self.assertEqual(len(resources), resources_count)

    def test_resource_available_from_detail_page(self):
        resource = FilteredResourceFactory()

        response = self.client.get('/api/filter/{id}/'.format(id=resource.id))
        r = json.loads(response.content.decode('utf8'))
        self.assertEqual(r['id'], resource.id)

    def test_delete_resource_via_api(self):
        resource = FilteredResourceFactory()

        self.client.delete('/api/filter/{id}/'.format(id=resource.id))

        self.assertFalse(FilteredResource.objects.all().exists())

    def test_can_create_image_via_api(self):
        img = ImageFactory()
        self.client.post('/api/filter/', data={'image': img.id, 'filter': 'edge'})

        self.assertTrue(FilteredResource.objects.all().exists())

# TODO reverse urls
