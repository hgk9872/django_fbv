from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    search_fields = ['title']


class CommentAdmin(admin.ModelAdmin):
    search_fields = ['content']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)