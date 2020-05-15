# Generated by Django 3.0.6 on 2020-05-11 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist_files',
            name='files',
            field=models.FileField(blank=True, upload_to='todo/files/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='todolist_images',
            name='image',
            field=models.ImageField(blank=True, upload_to='todo/images/%Y/%m'),
        ),
    ]