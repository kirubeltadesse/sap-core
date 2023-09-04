from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from backend.models import Event, Category
from django.contrib.auth.models import User
from django.utils import timezone


class TestEvent(APITestCase):
    # test if the url is working
    def test_view_events(self):
        url = reverse("api:list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # test if the data is correct inserted
    def create_event(self):
        self.test_category = Category.objects.create(name="django")

        self.studentUser = User.objects.create_user(
            username="test_user1", password="123456789"
        )

        self.mentorUser = User.objects.create_user(
            username="test_user2", password="123456789"
        )

        data = {
            "category_id": 1,
            "title": "Event Title",
            "content": "Event Content",
            "slug": "event-title",
            "student": self.studentUser,
            "mentor": self.mentorUser,
            "start_date": timezone.now(),
            "end_date": timezone.now(),
            "status": "published",
        }
        url = reverse("api:list")
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
