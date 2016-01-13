import musicbrainzngs
from optparse import make_option
from django.conf import settings
from django.core.management.base import BaseCommand
from common.models import Album


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option(
            '-f', '--full',
            dest='full',
            action='store_true',
            default=False
        ),
    )

    def handle(self, **options):
        musicbrainzngs.set_useragent(settings.MB_APP, settings.MB_VERSION, settings.MB_CONTACT)
        if options['full']:
            albums = Album.objects.filter(image='')
        else:
            albums = Album.objects.filter(is_get_image=False)
        for album in albums:
            print 'ALBUM: ', album
            for release in album.releases.all():
                try:
                    data = musicbrainzngs.get_image_list(release.mbid)
                    url = ''
                    for image in data['images']:
                        if 'Front' in image['types'] and image['approved']:
                            url = image['thumbnails']['large']
                    if url:
                        print '+'
                        album.image = url
                        break
                except musicbrainzngs.musicbrainz.ResponseError:
                    pass
            if not album.image:
                print '-'
            album.is_get_image = True
            album.save()
        print 'FINISHED'
