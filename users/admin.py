from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# admin.site.register(User, UserAdmin)


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "Personal Info",
            {"fields": ("nickname", "birthday", "avatar")},
        ),
    )

    list_display = ("email", "nickname", "birthday", "is_active", "is_staff")

    filter_horizontal = ()
