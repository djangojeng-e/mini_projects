from django.contrib import admin
from django.urls import path
from .views import IndexView, DetailView, DeleteView

app_name = 'todo'

urlpatterns = [
    path('', IndexView.as_view(), name='todolist'),
    path('detail/<int:pk>/', DetailView.as_view(), name="todolist_detail"),
    path('delete/<int:pk>/', DeleteView.as_view(), name="todolist_delete"),
]
