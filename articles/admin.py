from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import User, Article


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_staff', 'is_superuser', 'role')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

    list_filter = ('is_staff', 'is_superuser', 'role')


admin.site.register(User, CustomUserAdmin)

admin.site.register(Article)
