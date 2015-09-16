from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from common import views

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', views.MainPage.as_view(), name='main_page'),
    url(r'^a/', include(admin.site.urls,)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)

urlpatterns += staticfiles_urlpatterns()
