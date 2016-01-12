import musicbrainzngs
from optparse import make_option
from django.conf import settings
from django.core.management.base import BaseCommand
from django.db.models import F
from common.models import Artist, Release


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option(
            '-c', '--changed',
            dest='changed',
            action='store_true',
            default=False
        ),
    )

    def handle(self, **options):
        musicbrainzngs.set_useragent(settings.MB_APP, settings.MB_VERSION, settings.MB_CONTACT)
        if options['changed']:
            artists = Artist.objects.exclude(lastfm_mbid=F('mbid'))
        else:
            artists = Artist.objects.filter(lastfm_playcount__gt=settings.LASTFM_MIN_PLAY_COUNT, mbid__gt='')
        for artist in artists:
            print artist.title
            if options['changed']:
                # deleting old releases and albums
                artist.max_year = 0
                for old_release in artist.releases.all():
                    old_release.delete()
                for old_album in artist.albums.all():
                    old_album.delete()
                artist.save()
            # getting new releases
            for release_type in settings.MB_RELEASE_TYPES:
                limit = 100
                offset = 0
                parsed = 0
                cont = True
                while cont:
                    releases = musicbrainzngs.browse_releases(artist=artist.mbid,
                                                              release_type=[release_type],
                                                              release_status=settings.MB_RELEASE_STATUSES,
                                                              limit=limit,
                                                              offset=offset)
                    for release in releases['release-list']:
                        parsed += 1
                        album, created = Release.objects.get_or_create(mbid=release.get('id'), artist=artist)
                        if created:
                            print 'new: ', release.get('id'), release.get('title')
                            album.date = release.get('date')
                            if album.date:
                                album.year = release.get('date').split('-')[0]
                            album.title = release.get('title')
                            album.country = release.get('country')
                            album.type = release_type
                            album.save()
                    if parsed < releases['release-count']:
                        offset += limit
                    else:
                        cont = False
            print '###'
        print 'releases - ok'
