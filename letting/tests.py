from django.test import TestCase, Client
from django.urls import reverse


class SiteTestCase(TestCase):
    def setUp(self):
        pass

    def test_letting_index_status_code_should_be_200(self):
        client = Client()
        path = reverse("letting:index")
        response = client.get(path)
        assert response.status_code == 200

    def test_letting_index_page_should_have_title(self):
        client = Client()
        path = reverse("letting:index")
        response = client.get(path)
        assert str(response.content).find("<title>Lettings</title>") > 0
