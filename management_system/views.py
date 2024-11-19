from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from management_system.models import Dish, DishType, Cook


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
    paginate_by = 3


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


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    template_name = "cook/cook_detail.html"


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    fields = (
        "username",
        "password",
        "first_name",
        "last_name",
        "email",
        "years_of_experience",
    )
    template_name = "cook/cook_form.html"
    success_url = reverse_lazy("management_system:cooks-list")


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    template_name = "cook/cook_confirm_delete.html"
    success_url = reverse_lazy("management_system:cooks-list")


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    fields = [
        "username",
        "password",
        "first_name",
        "last_name",
        "email",
        "years_of_experience",
    ]

    template_name = "cook/cook_form.html"
    success_url = reverse_lazy("management_system:cook-list")
