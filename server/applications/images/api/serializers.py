import hashlib

from django.core.files.base import ContentFile
from rest_framework import serializers

from applications.images.models import Image


class ImageSerializer(serializers.ModelSerializer):
    base64_image = serializers.CharField(write_only=True, style={'base_template': 'textarea.html'})

    class Meta:
        model = Image
        fields = ('id', 'image', 'creation_date', 'base64_image')
        read_only_fields = (
            'image',
        )

    def create(self, validated_data):
        base64_text = validated_data.pop('base64_image', None)
        instance = super().create(validated_data)
        if base64_text:
            instance.base64_file.save(
                self._get_text_hash(base64_text),
                ContentFile(base64_text)
            )
        return instance

    def _get_text_hash(self, text):
        return hashlib.md5(text.encode('utf-8')).hexdigest()
