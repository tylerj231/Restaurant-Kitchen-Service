from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTest(TestCase):
    def setUp(self):
        self.client = Client(address="127.0.0.1")
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin", password="test231"
        )
        self.client.force_login(self.admin_user)
        self.cook = get_user_model().objects.create_user(
            username="cook", password="test123", years_of_experience=25
        )

    def test_cook_years_of_experience_listed(self):
        """
        Test that checks if years_of_experience is listed on the cook admin panel
        :return:
        """
        url = reverse("admin:management_system_cook_changelist")
        response = self.client.get(url)
        self.assertContains(response, self.cook.years_of_experience)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.cook.years_of_experience, 25)

    def test_cook_years_of_experience_listed_on_detail(self):
        """
        Test that checks if years_of_experience is listed on the cook detail admin panel
        :return:
        """
        url = reverse("admin:management_system_cook_change", args=[self.cook.pk])
        response = self.client.get(url)
        self.assertContains(response, self.cook.years_of_experience)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.cook.years_of_experience, 25)

    def test_if_years_of_experience_listed_in_add_info(self):
        """
        Test that check of years_of_experience is listed on the cook creation form in admin panel
        :return:
        """
        url = reverse("admin:management_system_cook_add")
        response = self.client.get(url)
        self.assertContains(response, "years_of_experience")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.cook.years_of_experience, 25)
