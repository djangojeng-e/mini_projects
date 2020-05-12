from django.shortcuts import render
from .models import TodoList, TodoList_files, TodoList_images
from django.views import generic

# Create your views here.


class IndexView(generic.ListView):
    context_object_name = 'to_do_list'
    

    def get_queryset(self):
        return TodoList.objects.all()


class DetailView(generic.DetailView):
    model = TodoList
    context_object_name = 'todolist'
    
    def get_queryset(self):
        return TodoList.objects.all()
