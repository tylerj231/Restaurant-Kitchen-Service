from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from management_system.models import DishType, Dish


class PrivateDishPageTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test-user", password="test123"
        )
        self.client.force_login(self.user)

    def test_retrieve_dish_list(self):
        """
        Test that checks whether logged-in user receives list of dishes
        :return:
        """
        dish_type = DishType.objects.create(name="Test DishType")
        first_dish = Dish.objects.create(
            name="Test Dish", description="Test Dish", price=10, dish_type=dish_type
        )
        second_dish = Dish.objects.create(
            name="Test Dish_2", description="Test Dish_2", price=15, dish_type=dish_type
        )

        response = self.client.get(reverse("management_system:dish-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "dish/dish_list.html")

    def test_retrieve_dish_detail(self):
        dish_type = DishType.objects.create(name="Test DishType")

        dish = Dish.objects.create(
            name="Test Dish", description="Test Dish", price=10, dish_type=dish_type
        )

        response = self.client.get(
            reverse("management_system:dish-detail", kwargs={"pk": dish.pk})
        )

        self.assertEqual(response.status_code, 200)
