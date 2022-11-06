from rest_framework.response import Response
from rest_framework.decorators import api_view
from musicapp.models import Artiste, Song, Lyrics
from musicapp.API.serializers import ArtisteSerializer, SongSerializer, LyricsSerializer
from django.template.context_processors import request


@api_view(['GET', 'POST'])
def artiste_list (request):
    if request.method == 'GET':
    
        artiste = Artiste.objects.all()
        artiste_serializer = ArtisteSerializer(artiste, many=True)
        return Response(artiste_serializer.data)
    
    if request.method == 'POST':
        artiste_serializer = ArtisteSerializer(data=request.data)
        if artiste_serializer.is_valid():
            artiste_serializer.save()
            return Response(artiste_serializer.data)
        else:
            return Response(artiste_serializer.errors)
        
@api_view()    
def song_details (request, pk):
    song = Song.objects.get(pk=pk)
    song_serializer = SongSerializer(song)
    return Response(song_serializer.data)

@api_view()    
def all_song_details (request):
    all_song = Song.objects.all()
    all_song_serializer = SongSerializer(all_song, many=True)
    return Response(all_song_serializer.data)

@api_view()    
def song_lyrics (request, pk):
    lyrics = Lyrics.objects.get(pk=pk)
    lyrics_serializer = LyricsSerializer (lyrics)
    return Response(lyrics_serializer.data)

@api_view()    
def all_song_lyrics (request):
    all_lyrics = Lyrics.objects.all()
    all_lyrics_serializer = LyricsSerializer (all_lyrics, many=True)
    return Response(all_lyrics_serializer.data)