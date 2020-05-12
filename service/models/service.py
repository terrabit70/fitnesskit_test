import uuid
from django.db import models


class Service(models.Model):
    service_id = models.UUIDField(blank=False, null=False, primary_key=True, default=uuid.uuid4)
    name = models.CharField(blank=False, null=False, max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} : {self.service_id}'
