from django import forms
from .models import Blog


class AddNewBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'photo', 'blog_text', 'autor']

        labels = {
            'title': 'Заголовок статьи',
            'photo': 'Фото',
            'blog_text': 'Текст статьи',
            'autor': 'Автор',
        }

        widgets = {
            'blog_text': forms.Textarea()
        }

        error_messages = {
            'tittle':
                {
                    'max_length': 'Слишком много символов',
                    'required': 'Введите хотя бы 1 символ'
                },
            'blog_text':
                {
                    'max_length': 'Слишком много символов',
                    'required': 'Введите хотя бы 1 символ'
                },

            'autor':
                {
                    'max_length': 'Слишком много символов',
                    'required': 'Введите хотя бы 1 символ'
                },
        }
