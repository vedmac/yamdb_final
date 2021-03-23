from rest_framework import filters

from .models import Categories, Genres


class CustomFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        category_slug = request.query_params.get("category")
        genre_slug = request.query_params.get("genre")
        name = request.query_params.get("name")
        year = request.query_params.get("year")
        if genre_slug:
            genre_id = Genres.objects.get(slug=genre_slug).id
            return queryset.filter(genre=genre_id)
        if category_slug:
            category_id = Categories.objects.get(slug=category_slug).id
            return queryset.filter(category=category_id)
        if name:
            return queryset.filter(name__contains=name)
        if year:
            return queryset.filter(year=year)
        return queryset
