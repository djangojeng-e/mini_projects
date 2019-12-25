from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView

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
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form': form})
