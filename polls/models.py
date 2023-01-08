from django.db import models

# Create your models here.


class Images_all(models.Model):
    name_images = models.CharField(max_length=500)
    web_name = models.CharField(max_length=500)
    json_images = models.JSONField()

    def __str__(self):
        return self.name_images