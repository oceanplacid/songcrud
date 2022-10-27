from django.contrib import admin
from .models import Artiste, Song, Lyrics

class SongAdmin(admin.ModelAdmin):
    pass

admin.site.register (Artiste, SongAdmin)
admin.site.register (Song, SongAdmin)
admin.site.register (Lyrics, SongAdmin)
