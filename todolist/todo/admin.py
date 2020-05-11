from django.contrib import admin
from .models import TodoList, TodoList_files, TodoList_images
# Register your models here.


class TodoListAdmin(admin.ModelAdmin):
    pass 


class TodoList_imagesAdmin(admin.ModelAdmin):
    pass


class TodoList_filesAdmin(admin.ModelAdmin):
    pass


admin.site.register(TodoList, TodoListAdmin)
admin.site.register(TodoList_images, TodoList_imagesAdmin)
admin.site.register(TodoList_files, TodoList_filesAdmin)

