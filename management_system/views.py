from lib2to3.fixes.fix_input import context

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic

from management_system.forms import (
    CookCreationForm,
    CookSearchForm,
    DishSearchForm,
    DishTypeSearchForm, RegistrationForm,
)
from management_system.models import Dish, DishType, Cook
from management_system.tests.test_models.test_models import User


class HomePageView(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dish_count"] = Dish.objects.count()
        context["dish_type_count"] = DishType.objects.count()
        context["cook_count"] = Cook.objects.count()

        return context


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    template_name = "dish/dish_list.html"
    form_class = DishSearchForm
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["name"] = name
        context["search_form"] = DishSearchForm(
            initial={"name": self.request.GET.get("name")}
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        dish_name = self.request.GET.get("name")
        if dish_name:
            return queryset.filter(name__icontains=dish_name)
        return queryset


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    template_name = "dish/dish_detail.html"


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    fields = "__all__"
    template_name = "dish/dish_form.html"
    success_url = reverse_lazy("management_system:dish-list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    fields = "__all__"
    template_name = "dish/dish_form.html"
    success_url = reverse_lazy("management_system:dish-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    template_name = "dish/dish_confirm_delete.html"
    success_url = reverse_lazy("management_system:dish-list")


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    template_name = "dish_type/dish_type_list.html"
    context_object_name = "dish_type_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["name"] = name
        context["search_form"] = DishTypeSearchForm(
            initial={"name": self.request.GET.get("name")}
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get("name", "")
        if name:
            return queryset.filter(name__icontains=name)
        return queryset


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    template_name = "dish_type/dish_type_form.html"
    success_url = reverse_lazy("management_system:dish-type-list")


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    template_name = "dish_type/dish_type_confirm_delete.html"
    success_url = reverse_lazy("management_system:dish-type-list")


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    template_name = "dish_type/dish_type_form.html"
    success_url = reverse_lazy("management_system:dish-type-list")


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    template_name = "cook/cook_list.html"
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["username"] = username
        context["search_form"] = CookSearchForm(initial={"username": username})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        username = self.request.GET.get("username")
        if username:
            return queryset.filter(username__icontains=username)
        return queryset


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    template_name = "cook/cook_detail.html"


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookCreationForm
    template_name = "cook/cook_form.html"
    success_url = reverse_lazy("management_system:cooks-list")


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    template_name = "cook/cook_confirm_delete.html"
    success_url = reverse_lazy("management_system:cooks-list")


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookCreationForm
    template_name = "cook/cook_form.html"
    success_url = reverse_lazy("management_system:cooks-list")

class CookRegisterView(SuccessMessageMixin, generic.CreateView):
    model = Cook
    form_class = RegistrationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"
    success_message = "You have successfully registered."
