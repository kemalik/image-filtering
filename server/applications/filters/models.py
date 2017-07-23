from django.db import models

from applications.filters.constants import FILTERS_CHOICE
from applications.images.models import Image


class FilteredResource(models.Model):
    image = models.ForeignKey(Image, verbose_name='Input image', related_name='filtered_image')
    filter = models.CharField('Filter', max_length=10, choices=FILTERS_CHOICE)
    result = models.ForeignKey(Image, verbose_name='Result image',
                               related_name='filter_type', null=True, blank=True)

    def __str__(self):
        return str(self.id)
