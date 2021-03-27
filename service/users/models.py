from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4


# Create your models here.


class User(AbstractUser):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    username = models.CharField(max_length=64, unique=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.username}'


class Author(models.Model):
    name = models.CharField(max_length=64, unique=True)
    birthday_year = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=64, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
