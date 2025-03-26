from django.contrib import admin
from .models import Post, Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'content', 'created_at', 'updated_at')
    
admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'content', 'created_at', 'updated_at')
admin.site.register(Comment, CommentAdmin)
