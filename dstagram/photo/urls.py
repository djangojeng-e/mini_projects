"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import DetailView

from .views import photo_list, CreateView, DeleteView, PhotoDeleteView, PhotoUploadView, PhotoUpdateView
from .models import Photo



# app_name 은 namespace로 사용되는 값. 템플릿에서 url 템플릿 태그를 사용할때 app_name 값이 설정 되어 있다면
# [app_name:URL패턴이름] 형태로 사용

# 제너릭 뷰인 DetailView 는 urls.py에서 인라인 코드로 작성 가능. path 함수에 인수로 전달할 때는 as_view안에 클래스 변수들을 설정해 사용

app_name = 'photo'

urlpatterns = [
    path('', photo_list, name='photo_list'),
    path('detail/<int:pk>/', DetailView.as_view(model=Photo, template_name='photo/detail.html'), name='photo_detail'),
    path('upload/', PhotoUploadView.as_view(), name='photo_upload'),
    path('delete/<int:pk>/', PhotoDeleteView.as_view(), name='photo_delete'),
    path('update/<int:pk>/', PhotoUpdateView.as_view(), name='photo_update'),
]
