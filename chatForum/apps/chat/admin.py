from django.contrib import admin

# Register your models here.

from .models import Message, Forum

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'room', 'timestamp')
    readonly_fields = ('id', 'timestamp')

class ForumAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'admin', 'image', 'created_on')
    readonly_fields = ('id', 'created_on')

admin.site.register(Message, MessageAdmin)
admin.site.register(Forum, ForumAdmin)