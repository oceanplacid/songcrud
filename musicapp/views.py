from django.shortcuts import render

from .models import Artiste, Song, Lyrics
from django.http import JsonResponse


def music_list (request):
    artiste = Artiste.objects.all()
    song = Song.objects.all()
    lyrics = Lyrics.objects.all()
    data = {'artiste': list(artiste.values()), 'song': list(song.values()), 'lyrics': list(lyrics.values())}
    
    return JsonResponse(data)
    
def song_details(request, pk):
    song_details = Song.objects.get(pk=pk)
    song_data = {'title': song_details.title, 'date-released': song_details.date_released, 'likes': song_details.likes,}
    return JsonResponse(song_data)