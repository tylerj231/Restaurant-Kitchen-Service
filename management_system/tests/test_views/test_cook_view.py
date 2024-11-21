from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from management_system.models import Cook


class PrivateCookViewTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test-user",
            password="test1234",
        )
        self.client.force_login(self.user)

    def test_retrieve_cook_list_view(self):
        """
        Test that checks if the cook list view is returned for the logged-in user
        :return:
        """

        Cook.objects.bulk_create(
            [
                Cook(
                    username="cook-1",
                    password="1234test",
                ),
                Cook(
                    username="cook-2",
                    password="1234test",
                ),
                Cook(
                    username="cook-3",
                    password="12345test",
                ),
            ]
        )

        url = reverse("management_system:cooks-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


def test_retrieve_cook_detail_view(self):
    """
    Test that checks if the cook detail view is returned for particular cook for the logged-in user
    :return:
    """
    cook = Cook.objects.create(
        username="cook-1",
        password="1234test",
    )

    url = reverse("management_system:cook-detail", kwargs={"pk": cook.pk})
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, "cook/cook_detail.html")
