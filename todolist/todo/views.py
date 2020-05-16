from django.shortcuts import render, redirect, HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from datetime import date, datetime
from .models import TodoList, TodoList_files, TodoList_images
from .forms import TodoCreateForm
# Create your views here.


def delete_todo(request, pk):
    t = TodoList.objects.get(pk=pk)
    t.delete() 
    return redirect('/')


class IndexView(generic.ListView):
    context_object_name = 'to_do_list'
    

    def get_queryset(self):
        return TodoList.objects.all()


class DetailView(generic.DetailView):
    model = TodoList
    context_object_name = 'todolist'
    
    def get_queryset(self):
        return TodoList.objects.all()


class DeleteView(generic.DeleteView):
    model = TodoList
    success_url = '/'
    template_name = 'todo/delete.html'



class UpdateView(generic.UpdateView):
    model = TodoList
    fields = ['name', 'description', 'date_deadline']
    template_name = 'todo/update.html'
    success_url = "/"



def TodoCreate(request):
    if request.method == "POST":
        
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            try: 
                name = request.POST['name']
                description = request.POST['description']
                date_deadline = request.POST['date_deadline']
                images = request.FILES.getlist('images')
                files = request.FILES.getlist('files')
                date_created= date.today()

        # valid 한 date_deadline value 를 넣지 않았을때 
        # 막을 방법이 없음. 
        # date_created 가 date_deadline 보다 지난 날짜에 생성도 되는 문제점

                t = TodoList.objects.create(
                name=name, 
                description=description,
                date_created=date_created, 
                date_deadline=date_deadline,
                )
                t.save()

                for image in images:
                    TodoList_images.objects.create(todo=t, image=image)

                for file_in_list in files:
                    TodoList_files.objects.create(todo=t, files=file_in_list)

                return redirect('/')
            except ValueError:
                return HttpResponse('enter the right value for the date')
        else:       
            return render(request, 'todo/create.html', {'form': form})     
    else:
        form = TodoCreateForm()
        return render(request, 'todo/create.html', {'form': form})