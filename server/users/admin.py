from django.contrib import admin
from users.models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models

class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('user_name', 'email',)
    list_filter = ('user_name', 'email', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('user_name', 'id', 'email', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('user_name', 'email', 'image')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('bio',)})
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':20, 'cols':60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_name', 'email', 'password1', 'password2', 'is_active', 'is_staff',),}
        ),
    )

admin.site.register(NewUser, UserAdminConfig)
