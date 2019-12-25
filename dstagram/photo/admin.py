from django.contrib import admin
from .models import Photo
# Register your models here.

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'created', 'updated']
    raw_id_fields = ['author']
    list_filter = ['created', 'updated', 'author']
    search_fields = ['text', 'created']
    ordering = ['-updated', '-created']


# list_display = ['id', 'author', 'created', 'updated'] 목록에 보일 필드를 설정.
# raw_id_fields : ForeignKey 필드 경우, 연결된 모델의 객체 목록을 출력하고 선택해야함. 목록이 너무 길 경우 불편해짐.
# raw_id_fields 로 설정, 값을 써넣는 형태로 바뀌고 검색 기능을 사용해 선택할수 있음.

# list_filter : 필터 기능을 사용할 필드를 선택

# search_fields : 검색 기능을 통해 검색할 필드를 선택. ForeignKey 필드는 설정할수 없음.

# ordering : 모델의 기본 정렬값이 아닌 관리자 사이트에서 기본으로 사용할 정렬값을 설정.

# admin.site.register(Photo)