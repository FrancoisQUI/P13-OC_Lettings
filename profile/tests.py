from django.test import TestCase, Client
from django.urls import reverse

from .models import Profile


class SiteTestCase(TestCase):
    def setUp(self):
        pass

    def test_profiles_index_status_code_should_be_200(self):
        client = Client()
        path = reverse("profile:index")
        response = client.get(path)
        assert response.status_code == 200

    def test_profiles_index_page_should_have_title(self):
        client = Client()
        path = reverse("profile:index")
        response = client.get(path)
        assert str(response.content).find("<title>Profiles</title>") > 0
