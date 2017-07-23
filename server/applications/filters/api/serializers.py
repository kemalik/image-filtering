from rest_framework import serializers

from applications.filters.models import FilteredResource


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilteredResource
        fields = ('id', 'image', 'filter', 'result')
        read_only_fields = (
            'result',
        )
