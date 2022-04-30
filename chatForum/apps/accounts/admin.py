from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'is_staff', 'has_logged_in', 'image')
    readonly_fields = ('id',)

admin.site.register(User, UserAdmin)