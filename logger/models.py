from django.db import models
from django.utils import timezone


class Log(models.Model):
    path = models.CharField(max_length=100)
    method = models.CharField(max_length=10)
    execution_time_sec = models.FloatField()
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.path
