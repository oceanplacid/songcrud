from rest_framework import serializers
from musicapp.models import Artiste, Song, Lyrics
from datetime import datetime


class ArtisteSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    age = serializers.IntegerField()
    
    def create(self, validated_data):
        return Artiste.objects.create(**validated_data)
    
class SongSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField()
    date_released = serializers.DateTimeField()
    likes = serializers.IntegerField()
    artiste_id = serializers.CharField()
    
    
class LyricsSerializer (serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    content = serializers.CharField()
    song_id = serializers.CharField()