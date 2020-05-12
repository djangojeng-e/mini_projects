from django.contrib import admin
from django.urls import path
from .views import IndexView, DetailView

app_name = 'todo'

urlpatterns = [
    path('', IndexView.as_view(), name='todolist'),
    path('detail/<int:pk>/', DetailView.as_view(), name="todolist_detail"),
]
