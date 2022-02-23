from .models import Category, Movies


def menu_links(request):

    category_links = Category.objects.all()
    movie_links = Movies.objects.all()
    return dict(category_links=category_links, movie_links=movie_links)
