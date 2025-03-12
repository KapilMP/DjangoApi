from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from books.models import Book
from .serializers import BookSerializer


class BookAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
