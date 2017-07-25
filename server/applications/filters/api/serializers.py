from rest_framework import serializers

from applications.filters.models import FilteredResource
from applications.filters.tasks import apply_filter


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilteredResource
        fields = ('id', 'image', 'filter', 'result', 'status')

    def validate_image(self, image):
        if self.instance and self.instance.image_id != image.id:
            raise serializers.ValidationError("You can't update image")
        return image

    def validate_result(self, image):
        if not self.instance and image:
            raise serializers.ValidationError("You can't set result image")
        return image

    def validate_status(self, status):
        if not self.instance and status == 'done':
            raise serializers.ValidationError("You can't set status Done without result")
        return status

    def create(self, validated_data):
        instance = FilteredResource.objects.create(**validated_data)
        apply_filter(instance.id, instance.image_id, instance.filter)
        return instance

    def update(self, instance, validated_data):
        updated_filter = validated_data.get('filter', instance.filter)
        if updated_filter != instance.filter:
            instance.filter = updated_filter
            instance.status = 'in_progress'
            instance.save()
            apply_filter(instance.id, instance.image_id, instance.filter)
        elif validated_data.get('result') != instance.result:
            instance.result = validated_data.get('result', instance.result)
            instance.status = validated_data.get('status', instance.status)
            instance.save()

        return instance
