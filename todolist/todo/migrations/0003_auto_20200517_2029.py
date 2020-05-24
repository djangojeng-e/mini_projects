# Generated by Django 3.0.6 on 2020-05-17 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20200511_1242'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Contact_From')),
                ('email', models.EmailField(max_length=100, verbose_name='이메일')),
                ('phone_number', models.IntegerField(verbose_name='전화번호')),
                ('message', models.TextField(max_length=500, verbose_name='연락내용')),
            ],
            options={
                'verbose_name': 'Contact Us',
                'verbose_name_plural': 'Contact Us',
            },
        ),
        migrations.AlterModelOptions(
            name='todolist',
            options={'verbose_name': '투두리스트', 'verbose_name_plural': '투두리스트'},
        ),
    ]