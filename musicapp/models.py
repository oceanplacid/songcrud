from django.db import models
from django.template.defaultfilters import default
from datetime import datetime


class Artiste(models.Model):
    first_name = models.CharField(max_length = 50, blank=False, null = False)
    last_name = models.CharField(max_length = 50, blank = True, null = True)
    age = models.IntegerField(blank=False, null = False)
    
    def __str__(self):
        return self.first_name

class Song (models.Model):
    title = models.CharField(max_length = 100, blank=False, null = False)
    date_released = models.DateTimeField ()
    likes = models.IntegerField ()
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Lyrics (models.Model):
    content = models.TextField(max_length = 20000, blank = False, null = False, unique = True)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content
    
    
