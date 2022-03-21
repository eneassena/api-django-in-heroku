from django.shortcuts import render
from rest_framework import generics 
from rest_framework.response import Response
from rest_framework import status

from .models import Todo 
from .serializers import TodoSerializer
from todo.service import todo_service


# Create your views here.
class ListTodo(generics.ListAPIView):
	queryset = todo_service.get_todo_all()
	serializer_class = TodoSerializer


class CreateTodo(generics.ListCreateAPIView):
	queryset = todo_service.get_todo_all()
	serializer_class = TodoSerializer

	

	def listar(self, request):
		queryset = self.get_queryset()
		serializer = TodoSerializer(queryset)
		return Response(serializer.data, status=status.HTTP_200_OK)



class DetailTodo(generics.RetrieveAPIView):
	queryset = todo_service.get_todo_all()
	serializer_class = TodoSerializer
	

