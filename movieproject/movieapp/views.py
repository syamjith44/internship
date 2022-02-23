from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify

from .models import Movies, Category


def home(request):
    movies = Movies.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'index.html', context)


def movie_detail(request, category_slug, movie_slug):
    try:
        movie = Movies.objects.get(category__slug=category_slug, slug=movie_slug)
    except Exception as e:
        raise e
    return render(request, 'detail.html', {'movie': movie, })


def add(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        year = request.POST.get('year')
        image = request.FILES['image']
        slug = slugify(request.POST.get('title'))
        category = Category.objects.get(title=request.POST.get('category'))
        movie = Movies(title=title, year=year, description=description, image=image, slug=slug, category=category, )


        category.save()
        movie.save()
        return redirect('/')

    return render(request, 'add.html')


def update_movie(request, movie_slug):
    movie = Movies.objects.get(slug=movie_slug)

    if request.method == "POST":

        movie.title = request.POST.get('title')
        movie.slug = slugify(request.POST.get('title'))
        movie.description = request.POST.get('description')
        movie.year = request.POST.get('year')
        movie.image = request.FILES['image']
        movie.category = Category.objects.get(title=request.POST.get('category'))

        movie.save()

        return redirect('/')

    return render(request, 'update_movie.html')


def delete_movie(request, movie_slug):

    if request.method == "POST":
        movie = Movies.objects.get(slug=movie_slug)
        movie.delete()
        return redirect('')
    return render(request, 'delete_movie.html', )


def movie_by_category(request, category_slug=None):
    category_page = None
    movies = None
    if category_slug is not None:
        category_page = get_object_or_404(Category, slug=category_slug)
        movies = Movies.objects.all().filter(category=category_page,)
    else:
        movies = Movies.objects.all()

    return render(request, 'category.html', {'category': category_page, 'movies': movies, })
