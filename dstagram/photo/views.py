from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView, DeleteView, UpdateView

from .models import Photo


def photo_list(request):
    photos = Photo.objects.all()
    # photo = {
    #     'photos': photos
    # }
    return render(request, 'photo/list.html', {'photos': photos})

# 함수형 뷰 vs 클래스형 뷰


class PhotoUploadView(CreateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/upload.html'
    # template_name = 실제 사용할 템플릿을 설정

    # form_valid 메서드는 업로드를 끝낸후 이동할 페이지를 호출하기 위해 사용하는 메서드
    def form_valid(self, form):
        # 작성자는 현재 로그인 한 사용자로 설정
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            # 작성자를 설정하면, is_valid 메서드를 이용해 입력된 값들을 검증
            # 이상이 없다면 데이터베이스에 저장 후 메인페이지로 이동.
            form.instance.save()
            return redirect('/')
        else:
            # 이상이 있을 경우, 작성된 내용을 그대로 작성 페이지에 표시
            return self.render_to_response({'form': form})


class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'


class PhotoUpdateView(UpdateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/update.html'

