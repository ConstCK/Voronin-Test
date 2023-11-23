# Generated by Django 4.2.7 on 2023-11-23 16:25

import django.core.validators
from django.db import migrations, models
import isbn_field.fields
import isbn_field.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Имя автора')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
                ('published_in', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1800), django.core.validators.MaxValueValidator(2023)], verbose_name='Год издания')),
                ('isbn', isbn_field.fields.ISBNField(max_length=28, validators=[isbn_field.validators.ISBNValidator], verbose_name='ISBN')),
                ('author', models.ManyToManyField(to='library.author', verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
                'ordering': ['title'],
            },
        ),
    ]