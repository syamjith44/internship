# Generated by Django 4.0.2 on 2022-02-20 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('year', models.IntegerField()),
                ('image', models.ImageField(upload_to='gallery')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieapp.category')),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movies',
                'ordering': ('year',),
            },
        ),
    ]
