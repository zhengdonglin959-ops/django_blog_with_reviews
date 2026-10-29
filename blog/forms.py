from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """Форма добавления нового отзыва."""
    class Meta:
        model = Review
        fields = ('fio', 'email', 'text')
        labels = {
            'fio': 'ФИО',
            'email': 'Email',
            'text': 'Текст отзыва',
        }
        widgets = {
            'fio': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Иванов Иван Иванович',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'example@mail.ru',
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-textarea',
                'rows': 5,
                'placeholder': 'Поделитесь своими впечатлениями о блоге...',
            }),
        }
