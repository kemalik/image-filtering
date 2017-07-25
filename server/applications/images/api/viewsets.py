from rest_framework import viewsets

from applications.images.models import Image
from .serializers import ImageSerializer


class ImagesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows images to be viewed or edited.
    """
    queryset = Image.objects.all().order_by('-creation_date')
    serializer_class = ImageSerializer
