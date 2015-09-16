from django.contrib import admin
from common.models import Artist, Release, Album


class AlbumAdminInline(admin.TabularInline):
    model = Album
    fields = ('title', 'type', 'year', '_edit')
    readonly_fields = ('type', '_edit',)
    extra = 0

    def has_add_permission(self, request):
        return False

    def _edit(self, obj):
        return '<a href="/a/common/album/{id}/">Edit</a>'.format(id=obj.id) if obj.id else ''
    _edit.allow_tags = True
    _edit.__name__ = ''


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'lastfm_playcount', 'max_year', 'mbid', 'created')
    list_display_links = list_display
    search_fields = ('id', 'title', 'mbid',)
    inlines = (AlbumAdminInline,)


class ReleaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'artist', 'country', 'date', 'mbid',)
    list_display_links = list_display
    search_fields = ('id', 'title', 'mbid',)
    list_filter = ('type',)
    raw_id_fields = ('artist',)


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'artist', 'year',)
    list_display_links = list_display
    search_fields = ('id', 'title',)
    list_filter = ('type',)
    raw_id_fields = ('artist',)

    def get_object(self, request, object_id, from_field=None):
        self.obj = super(AlbumAdmin, self).get_object(request, object_id, from_field)
        return self.obj

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == 'releases' and getattr(self, 'obj', None):
            kwargs['queryset'] = self.obj.releases
        return super(AlbumAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Release, ReleaseAdmin)
admin.site.register(Album, AlbumAdmin)
