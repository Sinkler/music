from django.views.generic import ListView
from django.utils.timezone import now, localtime
from digg_paginator import DiggPaginator
from common.models import Artist


class MainPage(ListView):
    template_name = 'common/main.html'
    context_object_name = 'artists'
    paginate_by = 30
    paginator_class = DiggPaginator

    def get_queryset(self):
        artists = Artist.objects
        year = int(self.request.GET.get('year', 0))
        if year:
            artists = artists.filter(max_year=year)
        return artists.order_by('-max_year', '-updated_albums', '-lastfm_playcount')

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True, **kwargs):
        return DiggPaginator(queryset, per_page, orphans=orphans, allow_empty_first_page=allow_empty_first_page,
                             body=10, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MainPage, self).get_context_data(**kwargs)
        y = localtime(now()).year
        g = self.request.GET.get('year')
        context.update({
            'years': range(y, y - 5, -1),
            'year': int(g) if g else 0
        })
        return context
