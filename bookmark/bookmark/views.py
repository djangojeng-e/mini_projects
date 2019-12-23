from django.shortcuts import render
from .models import Bookmark
from django.views.generic.list import ListView

# Create your views here.

# def BookmarkListView(request):
#     pass

# 이번 앱은 모든 뷰를 클래스 형 뷰로 만들것입니다.
# 뷰에는 함수형 뷰와 클래스형 뷰가 잇다는것을 기억해야합니다.


class BookmarkListView(ListView):
    model = Bookmark


# ListView를 상속해서 사용
# model을 import 해서 사용
