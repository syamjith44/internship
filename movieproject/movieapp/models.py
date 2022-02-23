from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=False)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_url(self):
        return reverse('movieapp:movie_by_category', args=[self.slug])


    def __str__(self):
        return '{}'.format(self.title)


class Movies(models.Model):
    title = models.CharField(max_length=250,blank=True)
    slug = models.SlugField(unique=False)
    description = models.TextField()
    year = models.IntegerField()
    image = models.ImageField(upload_to='gallery')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ('year',)
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    def get_url(self):
        return reverse('movieapp:movie_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return '{}'.format(self.title)
