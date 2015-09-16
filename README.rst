This application gets your lastfm library and shows last releases from musicbrainz:

.. image:: https://d1ro8r1rbfn3jf.cloudfront.net/ms_29127/fWe4qCQSowvGfnl5WoAWB4M90Efjke/New%2BAlbums%2B2015-09-16%2B17-27-50.jpg?Expires=1442500204&Signature=D0P2rO-ggOjGFdzDHHlNIXm74daPzhODCWjVTFm87elT8rlInOWy~XE~0yJhA1p0~z1TDZSsFAPca44aeaUUYeSyVvHC7frBjqzQ7IG0dlImW6LFvffxDfKYfL7A-Dq4JpO6bw8DnwsdIpju6zIy6307stVhx6eE1KZZJQnWfEfdhisnaVIxrsk-DzqYIwCckZ2SWzh0P16YlTzgejJ-Xw-QAXFNxqBWb-TMVn9bnoniAsZjilIj0ms4NuHs4LO~Hm8AtCtSFACbzslxKpGJ1Xz61-tuUq1Hr-qYEZGTrFQukfZOEfrvK7RiJCiWXORIkC6ROzSPr6DLHWdCimTBfw__&Key-Pair-Id=APKAJHEJJBIZWFB73RSA
    :target: https://d1ro8r1rbfn3jf.cloudfront.net/ms_29127/fWe4qCQSowvGfnl5WoAWB4M90Efjke/New%2BAlbums%2B2015-09-16%2B17-27-50.jpg?Expires=1442500204&Signature=D0P2rO-ggOjGFdzDHHlNIXm74daPzhODCWjVTFm87elT8rlInOWy~XE~0yJhA1p0~z1TDZSsFAPca44aeaUUYeSyVvHC7frBjqzQ7IG0dlImW6LFvffxDfKYfL7A-Dq4JpO6bw8DnwsdIpju6zIy6307stVhx6eE1KZZJQnWfEfdhisnaVIxrsk-DzqYIwCckZ2SWzh0P16YlTzgejJ-Xw-QAXFNxqBWb-TMVn9bnoniAsZjilIj0ms4NuHs4LO~Hm8AtCtSFACbzslxKpGJ1Xz61-tuUq1Hr-qYEZGTrFQukfZOEfrvK7RiJCiWXORIkC6ROzSPr6DLHWdCimTBfw__&Key-Pair-Id=APKAJHEJJBIZWFB73RSA

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
