from django.db import models


class Post(models.Model):
    """Статья в блоге (оставлена из предыдущего задания)."""
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    short = models.TextField(verbose_name='Краткое описание')
    body = models.TextField(verbose_name='Текст статьи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Review(models.Model):
    """Запись в книге отзывов."""
    fio = models.CharField(max_length=200, verbose_name='ФИО')
    email = models.EmailField(verbose_name='Email')
    text = models.TextField(verbose_name='Текст отзыва')
    is_checked = models.BooleanField(default=False, verbose_name='Проверено')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.fio} — {self.text[:40]}'
