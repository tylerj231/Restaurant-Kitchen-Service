from django.contrib.auth import get_user_model
from django.test import TestCase
from management_system.models import Dish, DishType


class ModelsTests(TestCase):

    def test_dish_type_str(self):
        """
        Test that checks if the correct dish type str representation is returned
        :return:
        """
        dish_type = DishType.objects.create(name="Wraps")
        self.assertEqual(str(dish_type), "Wraps")

    def test_dish_str(self):
        """
        Test that checks if the correct dish str representation is returned
        :return:
        """

        dish_type = DishType.objects.create(name="Drinks")
        dish = Dish.objects.create(
            name="Pizza",
            description="Delicious",
            price=100,
            dish_type=dish_type,
        )
        self.assertEqual(str(dish), "Pizza")

    def test_cook_str(self):
        """
        Test that checks if the correct cook str representation is returned
        :return:
        """

        cook = get_user_model().objects.create(
            username="test",
            password="<PASSWORD>",
            first_name="Andrew",
            last_name="Smith",
        )
        self.assertEqual(str(cook), f"{cook.first_name} {cook.last_name}")

    def test_create_cook_with_years_of_experience(self):
        """
        Test that checks if the cook with year_of_experience is created correctly
        :return:
        """

        username = "Test"
        password = "test12333"
        years_of_experience = 10

        cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience,
        )
        self.assertEqual(cook.username, username)
        self.assertTrue(cook.check_password(password))
        self.assertEqual(cook.years_of_experience, years_of_experience)
