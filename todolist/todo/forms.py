from django import forms
import datetime


class TodoCreateForm(forms.Form):

    name = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class': 'input',
                'placeholder': '해야할일',
            }
        )
    )

    description = forms.CharField(
        max_length=200,
        widget=forms.Textarea(
            attrs={
                'class': 'textarea',
                'placeholder': '할일에 대한 디테일',
            }
        )
    )

    date_deadline = forms.DateField(initial=datetime.date.today,
    # initial = datetime.date.today 로 정해서, 적어도 오늘 날짜로 폼이 미리 채워져서 
    # 에러를 방지할수 있음.. 
        widget=forms.DateInput(format='%Y-%m-%d',
            attrs={
                'id': 'datepicker',
                'placeholder': 'YYYY-MM-DD',
            }
        )
    )

    images = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={
                'multiple': True,
                'class': 'file-input',
            }
        ), required=False,
    )

    files = forms.FileField(
        widget=forms.ClearableFileInput(
            attrs={
                'multiple': True,
                'class': 'file-input',
            }
        ), required=False,
    )
