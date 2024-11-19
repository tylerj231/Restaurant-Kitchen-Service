from django.urls import reverse
from django.test import TestCase, Client


class PublicHomePageTestCase(TestCase):
    """
    Test that checks whether unauthorised person receives information contained on the home page.
    """

    def test_no_login_required(self):
        url = reverse("management_system:index")
        result = self.client.get(url)
        self.assertEqual(result.status_code, 200)
