from django.views.generic import ListView
from digg_paginator import DiggPaginator
from common.models import Artist


class MainPage(ListView):
    template_name = 'common/main.html'
    context_object_name = 'artists'
    paginate_by = 30
    paginator_class = DiggPaginator

    def get_queryset(self):
        return Artist.objects.order_by('-max_year', '-lastfm_playcount')

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True, **kwargs):
        return DiggPaginator(queryset, per_page, orphans=orphans, allow_empty_first_page=allow_empty_first_page,
                             body=10,
                             **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MainPage, self).get_context_data(**kwargs)
        context.update(

        )
        return context
