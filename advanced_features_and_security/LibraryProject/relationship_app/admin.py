from django.contrib import admin

# Register your models here.
from .models import Author, Book, Library, Librarian, UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "role") 
    search_fields = ("user__username", "role") 

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
admin.site.register(UserProfile, UserProfileAdmin)