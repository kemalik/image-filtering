from django.db import models


class Image(models.Model):
    base64_file = models.FileField('Base64 file', upload_to='base64_files/%Y/%m/%d', null=True, blank=True)
    creation_date = models.DateTimeField('Creation date', auto_now_add=True)

    def __str__(self):
        return str(self.id)

    def image(self):
        if self.base64_file:
            return self.base64_file.file.read()
        return ''
