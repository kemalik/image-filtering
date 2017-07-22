from rest_framework import serializers

from applications.images.models import Image


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image', 'creation_date')