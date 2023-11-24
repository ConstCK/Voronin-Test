from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Reader


@api_view(['POST'])
def register(request):
    Reader.objects.create(name=request.data['name'], email=request.data['email'])
    return Response('Успешная регистрация пользователя')
