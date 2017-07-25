from django.db import models

from applications.filters.constants import FILTERS_CHOICE, STATUS_CHOICE
from applications.images.models import Image


class FilteredResource(models.Model):
    image = models.ForeignKey(Image, verbose_name='Input image', related_name='filtered_image')
    filter = models.CharField('Filter', max_length=10, choices=FILTERS_CHOICE)
    result = models.ForeignKey(Image, verbose_name='Result image',
                               related_name='filter_type', null=True, blank=True)
    status = models.CharField('Status', max_length=15, default='in_progress', choices=STATUS_CHOICE)

    def __str__(self):
        return str(self.id)
