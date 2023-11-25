from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = BookSerializer
    queryset = Book.objects.all()


