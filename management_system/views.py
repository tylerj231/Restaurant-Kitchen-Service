from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from management_system.models import Dish, DishType, Cook


@login_required
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


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    template_name = "dish_list.html"


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    template_name = "dish_detail.html"


class DishCreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Dish
    fields = "__all__"
    template_name = "dish_form.html"
    success_url = reverse_lazy("management_system:dish-list")


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    template_name = "dish_type_list.html"
    context_object_name = "dish_type_list"

class DishTypeCreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = DishType
    fields = "__all__"
    template_name = "dish_type_form.html"
    success_url = reverse_lazy("management_system:dish-type-list")


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    template_name = "cook_list.html"

class CookCreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Cook
    fields = ["username", "password", "first_name", "last_name", "email", "years_of_experience"]
    template_name = "cook_form.html"
    success_url = reverse_lazy("management_system:cook-list")
