# from django.test import TestCase
# import json
# from rest_framework import status
# from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
# from mixer.backend.django import mixer
# from users.models import User
# from todo_app.models import Project, Todo
# from todo_app.serializers import ProjectSerializer
# from todo_app.views import TodoModelViewSet
#
#
# # Create your tests here.
#
#
# class TestTodoViewSet(TestCase):
    # def setUp(self):

    # def test_get_list(self):
    #     factory = APIRequestFactory()
    #     request = factory.get('/api/todo/')
    #     view = TodoModelViewSet.as_view({'get': 'list'})
    #     response = view(request)
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # def test_create_guest(self):
    #     factory = APIRequestFactory()
    #     request = factory.post('/api/todo/', {'user': {"username": "AzineBeland.1865"}, 'todo': 'test do do do'},
    #                            format='json')
    #     view = TodoModelViewSet.as_view({'post': 'create'})
    #     response = view(request)
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # def test_create_admin(self):
    #     factory = APIRequestFactory()
    #     request = factory.post('/api/todo/',
    #                            {'project': {},
    #                             'user': {'username': 'AzineBeland.1865', 'email': 'blabla@gmail.com'},
    #                             'todo': 'test do do do'},
    #                            format='json')
    #     admin = User.objects.create_superuser('su', 'superuser@admin.com', 'superuser123456')
    #     force_authenticate(request, admin)
    #     view = TodoModelViewSet.as_view({'post': 'create'})
    #     response = view(request)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
