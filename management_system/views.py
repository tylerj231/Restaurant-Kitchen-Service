from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from management_system.models import Dish, DishType, Cook


def index(request: HttpRequest) -> HttpResponse:
    dish_count = Dish.objects.count()
    dish_type_count = DishType.objects.count()
    cook_count = Cook.objects.count()

    context = {
        'dish_count': dish_count,
        'dish_type_count': dish_type_count,
        'cook_count': cook_count,
    }
    return render(request, "index.html", context=context)


class DishListView(generic.ListView):
    model = Dish
    template_name = "dish_list.html"


class DishDetailView(generic.DetailView):
    model = Dish
    template_name = "dish_detail.html"


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "dish_type_list.html"
    context_object_name = "dish_type_list"


class CookListView(generic.ListView):
    model = Cook
    template_name = "cook_list.html"
