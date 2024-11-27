from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from instrumentarium.accounts.forms import CustomUserCreationForm, CustomUserChangeForm

User = get_user_model()


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    list_display = ('email', 'first_name', 'last_name')

    fieldsets = (
        ('Info', {'fields': ('email', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups')})
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", 'first_name', 'last_name', "password1", "password2"),
            },
        ),
    )

    ordering = ('email', )

    search_fields = ('email', 'first_name', 'last_name')

    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
