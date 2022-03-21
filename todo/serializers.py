from rest_framework import serializers 
from .models import Todo 


class TodoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Todo 
		ordering = ['-id']
		fields = ['id', 'title', 'body']
		