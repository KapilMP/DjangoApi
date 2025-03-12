from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Todo
from .serializer import TodoSerializer
from rest_framework.exceptions import NotFound


class ListTodo(APIView):  # list api view
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)


class DetailTodo(APIView):  # detail api view (specific pk)
    def get(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise NotFound(detail="Todo chain", code=status.HTTP_404_NOT_FOUND)

        serializer = TodoSerializer(todo)
        return Response(serializer.data)
