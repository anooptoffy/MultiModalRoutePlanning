from django.db import models

# Create your models here.

class Node(models.Model):
    node = models.CharField(max_length=512)
    longitude = models.FloatField()
    latitude = models.FloatField()
    routes = models.CharField(max_length=1000)
    spath = models.CharField(max_length=10000000)

    def __str__(self):
        return self.node
