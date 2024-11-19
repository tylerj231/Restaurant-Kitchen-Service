from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from management_system.models import Dish, DishType, Cook


@admin.register(Dish)
class DishModelAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "dish_type",
    )


@admin.register(DishType)
class DishTypeModelAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Cook)
class CookModelAdmin(UserAdmin):
    list_display = UserAdmin.list_display + (
        "first_name",
        "last_name",
        "years_of_experience",
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "years_of_experience",
                    )
                },
            ),
        )
    )
