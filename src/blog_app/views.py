from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnDict
from .models import Post
from .serializers import Postserializer
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST'])
def post_list_create(request):
    if request.method == 'GET' :
        post = Post.objects.all()
        serializer = Postserializer(post, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = Postserializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'message' : 'New Post created succesfully'
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)