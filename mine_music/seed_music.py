import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mine_music.settings')
django.setup()

from music.models import Song

songs = [
    {
        "title": "Odissi Classical Evening Raga",
        "artist": "Traditional Odissi Ensemble",
        "album": "Heritage of Odisha",
        "genre": "Classical",
        "audio_file_url": "https://upload.wikimedia.org/wikipedia/commons/7/7b/Odissi_music_sample.ogg",
        "cover_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Odissi_dancer.jpg/800px-Odissi_dancer.jpg",
    },
    {
        "title": "Sitar Morning Melody",
        "artist": "Ravi Shankar",
        "album": "Morning Ragas",
        "genre": "Classical",
        "audio_file_url": "https://upload.wikimedia.org/wikipedia/commons/8/87/Sitar_sample.ogg",
        "cover_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Sitar.jpg/800px-Sitar.jpg",
    }
]

for song_data in songs:
    item, created = Song.objects.get_or_create(title=song_data['title'], defaults=song_data)
    if created:
        print(f"Added {song_data['title']} successfully.")
    else:
        print(f"{song_data['title']} already exists.")
