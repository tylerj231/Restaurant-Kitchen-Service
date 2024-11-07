from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from management_system.models import Dish, DishType, Cook


# Register your models here.


@admin.register(Dish)
class DishModelAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "dish_type",)


@admin.register(DishType)
class DishTypeModelAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Cook)
class CookModelAdmin(UserAdmin):
    list_display = ("username", "first_name", "last_name",)
