from rest_framework.views import APIView
#from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Post
from .serializers import PostSerializers


class PostList(APIView):
    def get(self,request):
        posts = Post.objects.all()
        serializer = PostSerializers(posts, many=True)
        # if serializer.is_valid(raise_exception=True):
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = PostSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class PostDetail(APIView):
    def get(self,request,pk):
        post = Post.objects.get(pk = pk )
        serializer = PostSerializers(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializers(post, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializers(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

