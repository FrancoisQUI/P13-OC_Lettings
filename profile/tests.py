from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Profile


class ProfileIndexTestCase(TestCase):
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

class ProfileDetailTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="test_user")
        Profile.objects.create(user=user, favorite_city="test_user")

    def test_profile_detail_status_code_should_be_200(self):
        profile = Profile.objects.get(user__username="test_user")
        client = Client()
        path = reverse("profile:profile", kwargs={"username": profile.user.username})
        response = client.get(path)
        assert response.status_code == 200

    def test_profiles_detail_page_should_have_title(self):
        profile = Profile.objects.get(user__username="test_user")
        client = Client()
        path = reverse("profile:profile", kwargs={"username": profile.user.username})
        response = client.get(path)
        assert str(response.content).find(f"<title>{profile.user.username}</title>") > 0
