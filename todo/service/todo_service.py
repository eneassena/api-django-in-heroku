from ..models import Todo


def get_todo_all():
    todos = Todo.objects.filter().order_by('-id')  

    return todos