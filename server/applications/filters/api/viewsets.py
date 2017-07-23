from rest_framework import viewsets
from .serializers import ResourceSerializer
from applications.filters.models import FilteredResource


class ResourceViewSet(viewsets.ModelViewSet):
    queryset = FilteredResource.objects.all().order_by('-id')
    serializer_class = ResourceSerializer
