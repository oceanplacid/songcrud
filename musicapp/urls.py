from django.urls import path, include

from musicapp.views import music_list, song_details

urlpatterns = [
    path('list/', music_list, name='music-list'),
    path('<int:pk>', song_details, name='song-details'),
]