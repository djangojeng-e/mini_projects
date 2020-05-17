from django.db import models
from datetime import date
import datetime
from django.contrib.auth.models import User

# Create your models here.


class TodoList(models.Model):
    name = models.CharField(max_length=40, verbose_name="할일제목")
    description = models.TextField(max_length=200, verbose_name="할일세부사항")
    date_created = models.DateField(auto_now_add=True, verbose_name="생성날짜")
    date_deadline = models.DateField(verbose_name="데드라인")
    
    def remaining_days(self):
        delta = self.date_deadline - date.today()
        days = delta.days 
        return days

    def __str__(self):
        return f'{self.name} | {self.description} | {self.date_created} | {self.date_deadline}'

    class Meta:
        verbose_name = "투두리스트"
        verbose_name_plural = "투두리스트"

class TodoList_images(models.Model):
    todo = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='todo/images/%Y/%m', blank=True)


class TodoList_files(models.Model):
    todo = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    files = models.FileField(upload_to='todo/files/%Y/%m', blank=True)


class ContactUs(models.Model):
    name = models.CharField(max_length=100, verbose_name="Contact_From")
    email = models.EmailField(max_length=100, verbose_name="이메일")
    phone_number = models.CharField(max_length=12, verbose_name="전화번호")
    message = models.TextField(max_length=500, verbose_name="연락내용")
    is_processed = models.BooleanField(default=False, blank=True, verbose_name="처리 완료 하시겠습니까?")

    def is_it_processed(self):
        if self.is_processed:
            return "처리완료"
        else:
            return "처리대기"

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"