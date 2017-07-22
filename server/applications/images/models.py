from django.db import models
import base64

class Image(models.Model):
    image = models.FileField('Image', upload_to='images/%Y/%m/%d')
    creation_date = models.DateTimeField('Creation date', auto_now_add=True)

    def __str__(self):
        return self.id

    def as_base64(self):
        return base64.b64encode(self.image.file.read())
