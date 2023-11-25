from rest_framework import serializers

from .models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), many=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        fields = ['id', 'title', 'author', 'published_in', 'isbn']
        model = Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name']
        model = Author
