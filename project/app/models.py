from django.db import models


class Image(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return str(self.image)


class Gallery(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    autoplay = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    active_images = models.ManyToManyField("Image", blank=True)

