from django.shortcuts import render
from django.views.generic import DetailView

from .models import Bookmark
from django.views.generic.list import ListView

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

# 이번 앱은 모든 뷰를 클래스 형 뷰로 만들것
# 뷰에는 함수형 뷰와 클래스형 뷰가 잇다는것을 기억.

# ListView를 상속해서 사용
# model을 import 해서 사용


class BookmarkListView(ListView):
    model = Bookmark


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

# field 변수는 어떤 필드를 입력 받을것인지 결정
# success_url 은 글쓰기를 완료하고 이동할 페이지
# template_name_suffix 는 사용할 텐플릿의 접미사만 변경하는 설정값


class BookmarkDetailView(DetailView):
    model = Bookmark


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'


class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')