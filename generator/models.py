from django.db import models


class Img(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    img = models.ImageField(upload_to="imgenerator/")

    def __str__(self) -> str:
        return self.name
