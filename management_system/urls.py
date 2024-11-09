from django.urls import path, include
from .views import (
    index,
    DishListView,
    DishDetailView,
    DishCreateView,
    DishTypeListView,
    DishTypeCreateView,
    CookListView,
    CookCreateView,
    DishUpdateView,
    DishDeleteView,
    CookDetailView,
    CookUpdateView,
    CookDeleteView,
)

app_name = "management_system"

urlpatterns = [
    path("", index, name="index"),
    path("dishes", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
    path("dish_type/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish_type/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("cooks/", CookListView.as_view(), name="cooks-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path("cooks/<int:pk>/update/", CookUpdateView.as_view(), name="cook-update"),
    path("cooks/<int:pk>/delete/", CookDeleteView.as_view(), name="cook-delete"),
]
