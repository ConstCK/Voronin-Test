from rest_framework import serializers

from .models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Book
        depth = 1


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name']
        model = Author
