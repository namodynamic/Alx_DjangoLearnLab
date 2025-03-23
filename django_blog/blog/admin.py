from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_date' ]
    fields = ['title', 'content', 'image',
              'tags',  'author']
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author','content', 'created_at', 'updated_at']    
    
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)