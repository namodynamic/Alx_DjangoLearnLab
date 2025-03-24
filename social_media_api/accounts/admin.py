from django.contrib import admin

from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'email','first_name', 'last_name', 'bio', 'date_joined', 'updated_at', 'follower_count', 'following_count')

admin.site.register(CustomUser, CustomUserAdmin)
