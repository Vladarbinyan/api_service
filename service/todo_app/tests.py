from django.test import TestCase
import json
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from users.models import User
from todo_app.models import Project, Todo
from todo_app.serializers import ProjectSerializer
from todo_app.views import TodoModelViewSet


# Create your tests here.


class TestTodoViewSet(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='Boryan99',
            first_name='Boris',
            last_name='Ivanov',
            email='ccc@vvv.ru',
        )

        self.admin = User.objects.create_superuser(
            username='su',
            first_name='Admin',
            last_name='admin',
            email='superuser@admin.com',
            password='superuser123456'
        )
        self.project = Project(
            title='first project',
            repository='http://example.com',
            text='some text',
        )
        self.project.save()
        self.project.users.add(self.user)

    def test_get_list(self):
        response = self.client.get('/api/todo/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_guest(self):
        response = self.client.post(
            '/api/todo/',
            {'project': self.project.uuid, 'user': self.user.uuid, 'todo': 'get eggs',
             'text': 'new todo'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        self.client.login(username='su', password='superuser123456')
        response = self.client.post(
            '/api/todo/',
            {'project': self.project.uuid, 'user': self.user.uuid, 'todo': 'get eggs',
             'text': 'new todo'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
