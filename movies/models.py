from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=128)
    context_object_name = 'movies'