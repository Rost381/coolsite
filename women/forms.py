from django import forms
from django.core.exceptions import ValidationError

from .models import *

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)# Конструктор базового класса
        self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets = { # Для какого поля тот или иной стиль
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }
    #Собственный вылидатор
    def clean_title(self): #clean_ общее название
        title = self.cleaned_data['title']
        if len(title) > 250:
            raise ValidationError('Длина превышает 250 символов')

        return title
