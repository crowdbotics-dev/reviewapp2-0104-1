from django.conf import settings
from django.db import models


class AnotherModel(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )
    age = models.IntegerField()
