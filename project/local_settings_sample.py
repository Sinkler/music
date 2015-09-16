###########################
# REQUIRED
###########################
LASTFM_USER = 'YOUR_LASTFM_USER'  # username from lastfm

###########################
# OPTIONAL
###########################
LASTFM_MIN_PLAY_COUNT = 10  # minimal number of playbacks on lastfm for artist
MB_RELEASE_TYPES = ['album', 'ep', 'live', 'compilation']  # https://python-musicbrainzngs.readthedocs.org/en/latest/api/#musicbrainzngs.musicbrainz.VALID_RELEASE_TYPES
MB_RELEASE_STATUSES = ['official']  # https://python-musicbrainzngs.readthedocs.org/en/latest/api/#musicbrainzngs.musicbrainz.VALID_RELEASE_STATUSES
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'music.db',
    }
}
