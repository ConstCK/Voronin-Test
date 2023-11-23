from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from isbn_field import ISBNField

from datetime import datetime


class Book(models.Model):
    @staticmethod
    def current_year():
        return datetime.now().year

    title = models.CharField(max_length=128, verbose_name='Название')
    author = models.ManyToManyField('Author', verbose_name='Автор')
    published_in = models.PositiveIntegerField(validators=[MinValueValidator(1800), MaxValueValidator(current_year())],
                                               verbose_name='Год издания')
    isbn = ISBNField(verbose_name='ISBN')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['title']


class Author(models.Model):
    name = models.CharField(max_length=128, verbose_name="Имя автора", unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['name']
