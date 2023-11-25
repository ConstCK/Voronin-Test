from rest_framework import serializers

from .models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), many=True)

    class Meta:
        fields = ['title', 'author', 'published_in', 'isbn']
        model = Book
        depth = 1


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name']
        model = Author
