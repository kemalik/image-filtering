from django.db import models


class Image(models.Model):
    image = models.FileField('Image', upload_to='images')
    creation_date = models.DateTimeField('Creation date', auto_now_add=True)

    def __str__(self):
        return self.id
