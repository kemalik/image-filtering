import factory

from .models import FilteredResource
from applications.images.factories import ImageFactory


class FilteredResourceFactory(factory.DjangoModelFactory):
    class Meta:
        model = FilteredResource

    image = factory.SubFactory(ImageFactory)
    filter = 'edge'
    result = factory.SubFactory(ImageFactory)
    status = 'in_progress'

