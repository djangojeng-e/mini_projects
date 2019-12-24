from django.urls import path
from .views import BookmarkListView, BookmarkCreateView, BookmarkDetailView

urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'),
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
]

# bookmark/ 에 접속했을때, BookmarkListView.as_view() 라는 뷰가 호출됨
## 클래스 베이스는 as_view() 라고 꼭 붙여줘야 정상적으로 동작함.
# 마지막 인자인 name='list' 는 설정한 이름을 가지고 해당 URL 패턴을 찾을수 있도록 하는 역할
