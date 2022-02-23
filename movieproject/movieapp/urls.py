from django.urls import path
from . import views

app_name = 'movieapp'
urlpatterns = [

    path('', views.home, name='home'),
    path('detail/<slug:category_slug>/<slug:movie_slug>', views.movie_detail, name='movie_detail'),
    path('category/<slug:category_slug>/', views.movie_by_category, name='movie_by_category'),
    path('add', views.add, name='add'),
    path('update/<slug:movie_slug>', views.update_movie, name='update_movie'),
    path('delete/<slug:movie_slug>', views.delete_movie, name='delete_movie'),

]
