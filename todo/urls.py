from django.urls import path
from .views import ListTodo, DetailTodo, CreateTodo

app_label = 'todo'

urlpatterns = [
	path('<int:pk>/', DetailTodo.as_view()),
	path('', ListTodo.as_view()),
	path('create/', CreateTodo.as_view(), name='todo-create')
]


