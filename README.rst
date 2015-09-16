This application gets your lastfm library and shows last releases from musicbrainz:

.. image:: https://api.monosnap.com/rpc/file/download?id=OQapGOdXtIQaN1FW2jfW7ULWN5w0f6
    :target: https://api.monosnap.com/rpc/file/download?id=OQapGOdXtIQaN1FW2jfW7ULWN5w0f6

Installation
============

::

    cp project/local_settings_sample.py project/local_settings.py

Then change settings in project/local_settings.py

::

    virtualenv venv
    . venv/bin/activate
    pip install -Ur requirements.txt
    ./manage.py migrate
    ./manage.py createsuperuser

Loading/updating artists and releases
=====================================

::

    . venv/bin/activate
    ./manage.py artists
    ./manage.py releases
    ./manage.py albums
    ./manage.py covers

Run application
===============

::

    . venv/bin/activate
    ./manage.py runserver 8001

Discussion
==========

http://pyha.ru/forum/topic/9173
