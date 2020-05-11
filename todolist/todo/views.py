from django.shortcuts import render
from .models import TodoList, TodoList_files, TodoList_images
from django.views import generic

# Create your views here.


class IndexView(generic.ListView):
    context_object_name = 'to_do_list'
    template_name = 'todo/todo-lists.html' 

    def get_queryset(self):
        return TodoList.objects.all()
