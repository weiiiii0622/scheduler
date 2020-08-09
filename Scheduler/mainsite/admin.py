from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserRegistrationForm, UserChangeForm

# Register your models here.

User = get_user_model()

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserRegistrationForm

    list_display = ('account', 'email', 'is_admin', 'is_active')
    list_filter = ('is_admin', 'is_active')
    
    
    fieldsets = (
        (None, {'fields': ('account', 'email', 'password')}),
        ('Personal info', {'fields': ('date',)}),
        ('Permissions', {'fields': ('is_admin', 'is_active')}),
    )


    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('account', 'email', 'password1', 'password2', 'is_admin', 'is_active'),
        }),
    )
    
    search_fields = ('account', 'email')
    ordering = ('account',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
