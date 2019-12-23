from django.db import models

# Create your models here.

class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('site URL')

    def __str__(self):
        return f'이름 : {self.site_name}, 주소 : {self.url}'

