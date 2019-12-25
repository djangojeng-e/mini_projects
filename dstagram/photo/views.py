from django.shortcuts import render

# Create your views here.
from .models import Photo


def photo_list(request):
    photos = Photo.objects.all()
    # photo = {
    #     'photos': photos
    # }
    return render(request, 'photo/list.html', {'photos': photos})


