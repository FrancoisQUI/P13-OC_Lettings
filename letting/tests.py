from django.test import TestCase, Client
from django.urls import reverse

from .models import Address, Letting


class LettingIndexTestCase(TestCase):
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


class LettingDetailTestCase(TestCase):
    def setUp(self):
        address = Address.objects.create(number=99,
                                         street="test_street",
                                         city='test_city',
                                         state='XX',
                                         zip_code=99999,
                                         country_iso_code='XXX'
                                         )
        Letting.objects.create(title="test_letting", address=address)

    def test_letting_detail_status_code_should_be_200(self):
        letting = Letting.objects.get(title="test_letting")
        client = Client()
        path = reverse("letting:letting", kwargs={"letting_id": letting.id})
        response = client.get(path)
        assert response.status_code == 200

    def test_letting_detail_page_should_have_title(self):
        letting = Letting.objects.get(title="test_letting")
        client = Client()
        path = reverse("letting:letting", kwargs={"letting_id": letting.id})
        response = client.get(path)
        assert str(response.content).find(f"<h1>{letting.title}</h1>") > 0
