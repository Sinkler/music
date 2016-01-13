from django.core.management.base import BaseCommand
from django.utils.timezone import now
from common.models import Artist, Album


class Command(BaseCommand):
    def handle(self, **options):
        for artist in Artist.objects.all().order_by('lastfm_playcount'):
            print 'ARTIST: ', artist.title
            for release in artist.releases.filter(is_to_album=False):
                album, created = Album.objects.get_or_create(title=release.title, type=release.type, artist=artist)
                if created:
                    print 'NEW: ', release.title, release.year
                    album.year = release.year
                    artist.updated_albums = now()
                else:
                    if release.year:
                        album.year = release.year if not album.year else min(release.year, album.year)
                album.releases.add(release)
                album.save()
                release.is_to_album = True
                release.save()
            artist.max_year = 0
            for album in artist.albums.all():
                artist.max_year = max(artist.max_year, album.year)
            artist.save()
        print 'FINISHED'
