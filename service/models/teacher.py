from django.db import models


class Teacher(models.Model):
    short_name = models.CharField(blank=False, null=False, max_length=255)
    name = models.CharField(blank=False, null=False, max_length=255)
    position = models.CharField(blank=False, null=False, max_length=255)
    image = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.name
