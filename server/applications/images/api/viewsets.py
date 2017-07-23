from django.core.files.base import ContentFile
from rest_framework import viewsets
from .serializers import ImageSerializer
from applications.images.models import Image


class ImagesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows images to be viewed or edited.
    """
    queryset = Image.objects.all().order_by('-creation_date')
    serializer_class = ImageSerializer
