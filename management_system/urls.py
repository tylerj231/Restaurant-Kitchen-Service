from django.urls import path
from .views import (index,
                    DishListView,
                    DishDetailView,
                    DishTypeListView,
                    CookListView,)

app_name = "management_system"

urlpatterns = [
    path("", index, name="index"),
    path("dishes", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dish_type/", DishTypeListView.as_view(), name="dish-type-list"),
    path("cooks/", CookListView.as_view(), name="cooks-list"),
]
