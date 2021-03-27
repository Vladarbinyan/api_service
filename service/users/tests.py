from django.test import TestCase
import json
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
# from mixer.backend.django import mixer
# from users.models import User
from users.views import UserMixinViews, AuthorViewSet
from .models import Author


# Create your tests here.


class TestUserViewSet(TestCase):

    # def test_get_list(self):
    #     factory = APIRequestFactory()
    #     request = factory.get('/api/users/')
    #     view = UserMixinViews.as_view({'get': 'list'})
    #     response = view(request)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/authors/')
        view = AuthorViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_create_guest(self):
    #     factory = APIRequestFactory()
    #     request = factory.post('/api/users/',
    #                            {'username': 'VasyaAdmin777', 'first_name': 'Vasya', 'last_name': 'Petrov',
    #                             'email': 'chebu@mail.ru'},
    #                            format='json')
    #     view = UserMixinViews.as_view({'post': 'create'})
    #     response = view(request)
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    #
    # def test_create_admin(self):
    #     factory = APIRequestFactory()
    #     request = factory.post('/api/users/',
    #                            {'username': 'VasyaAdmin777', 'first_name': 'Vasya', 'last_name': 'Petrov',
    #                             'email': 'chebu@mail.ru'},
    #                            format='json')
    #     admin = User.objects.create_superuser('su', 'superuser@admin.com', 'superuser123456')
    #     force_authenticate(request, admin)
    #     view = UserMixinViews.as_view({'post': 'create'})
    #     response = view(request)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_get_detail(self):
    #     user = User.objects.create_user(username='Boryan99', first_name='Boris', last_name='Ivanov', email='ccc@vvv.ru',
    #                                     password='123123')
    #     client = APIClient()
    #     response = client.get("/")
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_detail(self):
        author = Author.objects.create(name='Pushkin', birthday_year=1799)
        client = APIClient()
        response = client.get(f'/api/authors/')
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestBookViewSet(APITestCase):

    def test_get_list(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# def test_edit_guest(self):
#     user = User.objects.create_user(username='Boryan99', first_name='Boris', last_name='Ivanov', email='ccc@vvv.ru',
#                                )
#     client = APIClient()
#     response = client.put(f'/api/users/{user.uuid}/', username='Boryan99', first_name='Boris', last_name='Petrov',
#                           email='ccc@vvv.ru',
#                           )
#     print(f'/api/users/{user.uuid}/', response)
#     self.assertEqual(response.status_code, status.HTTP_200_OK)
