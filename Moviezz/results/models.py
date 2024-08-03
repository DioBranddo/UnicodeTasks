from django.db import models

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=250)
    year = models.IntegerField()
    genre = models.CharField(max_length=250)
    poster = models.CharField(max_length=2083)