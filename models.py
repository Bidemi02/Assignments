from django.db import models
from datetime import datetime
# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    age = models.IntegerField()

class Lyric(models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    content = models.TextField(null = False, blank=True)
    song_id = models.CharField(max_length=400)    

class Song(models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date_released = models.DateField(default=datetime.today)
    likes = models.IntegerField(default=0, blank=True)
    song_id = models.CharField(max_length=400)

