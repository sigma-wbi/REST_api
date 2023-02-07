from django.db import models


class Log(models.Model):
    recordId = models.CharField(max_length=100)
    time = models.FloatField()
    data = models.TextField()
