from lastfmclient import LastfmClient
from django.conf import settings
from django.core.management.base import BaseCommand
from common.models import Artist


class Command(BaseCommand):
    def handle(self, **options):
        api = LastfmClient(api_key=settings.LASTFM_API_KEY, api_secret=settings.LASTFM_API_SECRET)
        page = 1
        cont = True
        while cont:
            request = api.user.get_top_artists(settings.LASTFM_USER, limit=100, page=page)
            cont = int(request['@attr']['page']) < int(request['@attr']['totalPages'])
            page += 1
            for p in request['artist']:
                artist, created = Artist.objects.get_or_create(lastfm_mbid=p.get('mbid'), title=p.get('name'))
                if created:
                    artist.mbid = p.get('mbid')
                    print 'new: ', p.get('mbid'), p.get('name')
                artist.lastfm_playcount = p.get('playcount')
                artist.save()
        print 'artists - ok'
