from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', )
