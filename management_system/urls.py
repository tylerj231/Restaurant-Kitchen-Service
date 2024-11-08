from django.urls import path, include
from .views import (index,
                    DishListView,
                    DishDetailView,
                    DishCreateView,
                    DishTypeListView,
                    DishTypeCreateView,
                    CookListView,
                    CookCreateView,)

app_name = "management_system"

urlpatterns = [
    path("", index, name="index"),
    path("dishes", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dish_type/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish_type/create/",DishTypeCreateView.as_view(), name="dish-type-create"),
    path("cooks/", CookListView.as_view(), name="cooks-list"),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
]
