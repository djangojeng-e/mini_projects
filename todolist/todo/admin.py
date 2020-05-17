from django.contrib import admin
from .models import TodoList, TodoList_files, TodoList_images
from .models import ContactUs
# Register your models here.


class TodoList_filesInline(admin.TabularInline):
    model = TodoList_files


class TodoList_imagesInline(admin.TabularInline):
    model = TodoList_images


class TodoListAdmin(admin.ModelAdmin):
    inlines = [TodoList_filesInline, TodoList_imagesInline]

    list_display = ('name', 'description', 'date_created', 'date_deadline', 'remaining_days')
    list_filter = ['date_created']


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'message', 'is_processed' ,'is_it_processed')
    list_filter = ['email']
    search_fields = ['email']

admin.site.register(TodoList, TodoListAdmin)
admin.site.register(ContactUs, ContactUsAdmin)