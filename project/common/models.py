from django.db import models


class Artist(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)
    updated_albums = models.DateTimeField(null=True, blank=True)
    lastfm_mbid = models.CharField(default='', max_length=255)
    lastfm_playcount = models.PositiveIntegerField(default=0)
    mbid = models.CharField(default='', max_length=255)
    title = models.CharField(max_length=255)
    max_year = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-lastfm_playcount']

    def __unicode__(self):
        return self.title


class Release(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    artist = models.ForeignKey(Artist, related_name='releases')
    mbid = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=20)
    date = models.CharField(max_length=255, default='', blank=True)
    year = models.PositiveIntegerField(default=0)
    country = models.CharField(max_length=255, default='', blank=True)
    image = models.URLField(max_length=255, default='', blank=True)
    is_to_album = models.BooleanField(default=False)

    class Meta:
        ordering = ['-year']

    def __unicode__(self):
        return self.title


class Album(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    artist = models.ForeignKey(Artist, related_name='albums')
    releases = models.ManyToManyField(Release, related_name='albums', blank=True)
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=20)
    year = models.PositiveIntegerField(default=0)
    image = models.URLField(max_length=255, default='', blank=True)
    is_get_image = models.BooleanField(default=False)

    class Meta:
        ordering = ['-year']

    def __unicode__(self):
        return self.title
