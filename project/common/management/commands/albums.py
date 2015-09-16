from django.core.management.base import BaseCommand
from common.models import Artist, Release, Album


class Command(BaseCommand):
    def handle(self, **options):
        for artist in Artist.objects.all():
            print artist.title
            for release in Release.objects.filter(artist=artist, is_to_album=False):
                album, created = Album.objects.get_or_create(title=release.title, type=release.type, artist=artist)
                if created:
                    print 'new: ', release.title, release.year
                    album.year = release.year
                else:
                    if release.year:
                        album.year = release.year if not album.year else min(release.year, album.year)
                album.releases.add(release)
                album.save()
                release.is_to_album = True
                release.save()
                artist.max_year = max(artist.max_year, album.year)
                artist.save()
            print '###'
        print 'albums - ok'
