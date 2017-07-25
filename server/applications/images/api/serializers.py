import base64
import binascii
import hashlib
from logging import getLogger

from django.core.files.base import ContentFile
from rest_framework import serializers

from applications.images.models import Image

logger = getLogger(__name__)


class ImageSerializer(serializers.ModelSerializer):
    base64_image = serializers.CharField(write_only=True, style={'base_template': 'textarea.html'})

    class Meta:
        model = Image
        fields = ('id', 'image', 'creation_date', 'base64_image')
        read_only_fields = (
            'image',
        )

    def validate(self, data):
        split_data = data['base64_image'].split('base64,')
        if len(split_data) < 2:
            raise serializers.ValidationError("Base64 no have extension")
        try:
            base64.b64decode(split_data[-1])
        except binascii.Error:
            raise serializers.ValidationError("No correct base64")
        return data

    def create(self, validated_data):
        base64_text = validated_data.pop('base64_image', None)
        instance = super().create(validated_data)

        file_name = self._get_text_hash(base64_text)
        instance.base64_file.save(
            file_name,
            ContentFile(base64_text)
        )
        logger.debug('Image saved as {image_name}'.format(image_name=file_name))
        return instance

    def _get_text_hash(self, text: str) -> str:
        return hashlib.md5(text.encode('utf-8')).hexdigest()
