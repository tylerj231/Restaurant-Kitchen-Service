from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from management_system.models import DishType


class DishTypeViewTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="user-test!",
            password="test123",
        )
        self.client.force_login(self.user)

    def test_retrieve_dish_type_list(self):
        """
        Test that checks whether logged-in user receives list of dish_types
        :return:
        """
        first_dish_type = DishType.objects.create(name="First DishType")
        second_dish_type = DishType.objects.create(name="Second DishType")

        url = reverse("management_system:dish-type-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "dish_type/dish_type_list.html")
