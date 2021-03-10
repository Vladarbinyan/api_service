from django.db import models
from users.models import User
from uuid import uuid4


# Create your models here.


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=64)
    repository = models.CharField(2084)
    text = models.TextField(max_length=4096)
    users = models.ManyToManyField(User)

    def __str__(self):
        return f"Project:\n{id}\n{self.name}\nUsers:\n{self.users}"


class Todo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    todo = models.CharField(max_length=128)
    text = models.TextField(max_length=512, blank=True)
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.todo} created on {self.create_date} is {'active' if self.is_active else 'not active'}!"
