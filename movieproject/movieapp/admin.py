from django.contrib import admin
from .models import Movies, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', ]
    prepopulated_fields = {'slug': ('title',)}



class MoviesAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'category', ]
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 20


admin.site.register(Category, CategoryAdmin)
admin.site.register(Movies, MoviesAdmin)
