from django.db import models


class Reader(models.Model):
    name = models.CharField(max_length=64, verbose_name="Имя")
    email = models.EmailField(unique=True)
    registered_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Пользователь библиотеки'
        verbose_name_plural = 'Пользователи библиотеки'
        ordering = ['registered_at']
