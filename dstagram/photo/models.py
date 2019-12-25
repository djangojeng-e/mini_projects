from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from django.urls import reverse


class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')
    # Foreign Key 를 사용하여, User 테이블과 관계를 만듦.
    # User 모델은, 장고에서 기본적으로 사용하는 사용자 모델
    # on_delete = models.CASCADE 는 연결된 모델이 삭제될 경우, 현재 모델의 값은 어떻게 할것 이냐 결정함.
    # 삭제 될때의 동작은 CASCADE, PROTECTED, SET_NULL, SET_DEFAULT, SET(), DO_NOTHING 등이 있다.

    ## related_name 은 연결된 객체에서 하위 객체의 목록을 부를때 사용할 이름.
    #### 어떤 user가 작성한 글을 불러 올때는 유저 객체에 user_photos 속성을 참조.

    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png')
    text = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # auto_now_add = True : 객체가 추가될때 자동으로 값을 설정
    # auto_now=True : 객체가 수정될때마다 자동으로 값을 설정

    class Meta:
        ordering = ['-updated']
        # ordering 은 해당 모델의 객체를 어떤 기준으로 정렬할것 인지 설정하는 옵션
        # -updated 로 설정 : 글 수정 시간의 내림차순으로 정렬될것.

    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d%H:%M:%S")

    # __str__메서드는 작성자의 이름과 글 작성일을 합친 문자열을 반환

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[str(self.id)])

    # get_absolute_url 은 객체의 상세 페이지의 주소를 반환하는 메서드
    # 객체 추가 혹은 수정햇을때 이동할 주소를 위해 호출
    # 템플릿에서 상세 화면으로 이동하는 링크를 만들때 호출
    # reverse 는 URL 패턴 이름을 가지고 해당 패턴을 찾아 주소를 만들어주는 함수
