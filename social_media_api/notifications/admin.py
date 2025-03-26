from django.contrib import admin
from .models import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'actor', 'verb', 'timestamp', 'is_read')
admin.site.register(Notification, NotificationAdmin)
