from django.contrib import admin
from .models import User, Profile
from django.contrib.auth.admin import UserAdmin

# Register your models here.




class CustomUserAdmin(UserAdmin):
    list_display = ("email", "is_staff")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    ordering = ("email",)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)