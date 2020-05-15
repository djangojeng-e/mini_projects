from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy

from .models import TodoList, TodoList_files, TodoList_images

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


class DeleteView(generic.DeleteView):
    model = TodoList
    success_url = ''
    template_name = 'todo/delete.html'




class UpdateView(generic.UpdateView):
    model = TodoList
    fields = ['name', 'description', 'date_deadline']
    template_name = 'todo/update.html'
    success_url = "/"