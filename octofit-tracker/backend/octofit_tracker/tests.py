from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Team, User, Activity, Workout, Leaderboard

class TeamTests(APITestCase):
    def test_create_team(self):
        url = reverse('team-list')
        data = {'name': 'Test Team'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class UserTests(APITestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Team1')
    def test_create_user(self):
        url = reverse('user-list')
        data = {'name': 'Test User', 'email': 'test@example.com', 'team': self.team.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ActivityTests(APITestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Team2')
        self.user = User.objects.create(name='User2', email='user2@example.com', team=self.team)
    def test_create_activity(self):
        url = reverse('activity-list')
        data = {'user': self.user.id, 'type': 'run', 'duration': 30}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class WorkoutTests(APITestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Team3')
        self.user = User.objects.create(name='User3', email='user3@example.com', team=self.team)
    def test_create_workout(self):
        url = reverse('workout-list')
        data = {'user': self.user.id, 'description': 'Pushups'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LeaderboardTests(APITestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Team4')
    def test_create_leaderboard(self):
        url = reverse('leaderboard-list')
        data = {'team': self.team.id, 'points': 100}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
