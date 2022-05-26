from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from sesh.models import Post, Area
from django.contrib.auth.models import User

class PostTests(APITestCase):
    def test_view_post(self):

        url = reverse('session_api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def create_post(self):

        self.test_area = Area.objects.create(name='North London')

        self.testuser1 = User.objects.create_superuser(
            username = 'test_user1', password = '123456789')

        self.client.login(username=self.testuser1.username, password='123456789')

        data = {"difficulty":'new', "time": 'new', "players_needed":'new', "description":'new', "player":1,}
        url = reverse('session_api:listcreate')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_update(self):
        client = APIClient()
        self.test_area = Area.objects.create(name='North London')
        self.testuser1 = User.objects.create_user(
            username='test_user1', password='123456789')
        self.testuser2 = User.objects.create_user(
            username='test_user2', password='123456789')
        test_post = Post.objects.create(area_id=1, difficulty='Beginner', time='15:00', players_needed='1', description='new', player_id=1)

        client.login(username=self.testuser1.username, password='123456789')

        url = reverse(('session_api:detailcreate'), kwargs={'pk':1})

        response = client.put(
            url, {
                "id": 1,
                "player": 1,
                "time": "19:00",
                "players_needed": '2',
                "description": 'updated'
            }, format='json'
        )
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_not_allowed_update(self):
        client = APIClient()
        self.test_area = Area.objects.create(name='North London')
        self.testuser1 = User.objects.create_user(
            username='test_user1', password='123456789')
        self.testuser2 = User.objects.create_user(
            username='test_user2', password='123456789')
        test_post = Post.objects.create(area_id=1, difficulty='Beginner', time='15:00', players_needed='1', description='new', player_id=1)

        client.login(username=self.testuser2.username, password='123456789')

        url = reverse(('session_api:detailcreate'), kwargs={'pk':1})

        response = client.put(
            url, {
                "id": 1,
                "player": 1,
                "time": "19:00",
                "players_needed": '2',
                "description": 'updated'
            }, format='json'
        )
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
