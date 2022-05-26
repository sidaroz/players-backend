from unicodedata import name
from django.test import TestCase
from django.contrib.auth.models import User
from sesh.models import Post, Area

class Test_Create_Post(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_area = Area.objects.create(name='North London')
        testuser1 = User.objects.create_user(
            username = 'test_user1', password = '123456789')
        test_post = Post.objects.create(area_id=1, difficulty='Beginner', time= '17:00', players_needed='3', description='ajbdfhga hdfgarefv sdhgfvagsf', player_id=1)

    def test_sesh_content(self):
        post = Post.objects.get(id=1)
        area = Area.objects.get(id=1)
        player = f'{post.player}'
        difficulty = f'{post.difficulty}'
        time = f'{post.time}'
        players_needed = f'{post.players_needed}'
        description = f'{post.description}'

        self.assertEqual(player, 'test_user1')
        self.assertEqual(difficulty, 'Beginner')
        self.assertEqual(time, '17:00')
        self.assertEqual(players_needed, '3')
        self.assertEqual(description, 'ajbdfhga hdfgarefv sdhgfvagsf')
        self.assertEqual(str(post), '17:00')
        self.assertEqual(str(area), 'North London')

