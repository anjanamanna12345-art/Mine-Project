import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mine_music.settings')
django.setup()

from music.models import Song

updates = {
    "Odissi Classical Evening Raga": {
        "audio_file_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
        "cover_image_url": "https://images.unsplash.com/photo-1514320291840-2e0a9bf2a9ae?w=800"
    },
    "Sitar Morning Melody": {
        "audio_file_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
        "cover_image_url": "https://images.unsplash.com/photo-1511379938547-c1f69419868d?w=800"
    }
}

for title, data in updates.items():
    songs = Song.objects.filter(title=title)
    for song in songs:
        song.audio_file_url = data["audio_file_url"]
        song.cover_image_url = data["cover_image_url"]
        song.save()
print("Music URLs updated successfully!")
