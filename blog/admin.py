from django.contrib import admin
from .models import Post, Review


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('fio', 'email', 'is_checked', 'created_at')
    list_filter = ('is_checked',)
    list_editable = ('is_checked',)
