from django.urls import path, include

from musicapp.API.views import artiste_list, song_details, all_song_details, song_lyrics, all_song_lyrics

urlpatterns = [
    path('list/', artiste_list, name='artiste-list'),
    path('all-songs/', all_song_details, name='all-songs'),
    path('lyrics/', all_song_lyrics, name='all-lyrics'),
    path('<int:pk>', song_details, name='song-details'),
    path('lyrics/<int:pk>', song_lyrics, name='song-lyrics'),
]