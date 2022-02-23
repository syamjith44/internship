from django.shortcuts import render
from movieapp.models import Movies
from django.db.models import Q


def searchResults(request):
    query = None
    products = None
    if 'q' in request.GET:
        query = request.GET.get('q').format()
        movies = Movies.objects.all().filter(Q(title__icontains=query) | Q(description__icontains=query))

    return render(request, 'search.html', {'query': query, 'movies': movies, })

