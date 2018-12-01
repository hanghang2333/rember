from django.db import models

class IMG(models.Model):
    img = models.ImageField(upload_to='upload')
    def __str__(self):
        return self.img