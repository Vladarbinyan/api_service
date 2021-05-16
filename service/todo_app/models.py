from django.db import models
from users.models import User
from uuid import uuid4


# Create your models here.


class Project(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    title = models.CharField(max_length=64)
    repository = models.TextField(max_length=2084)
    text = models.TextField(max_length=4096)
    users = models.ManyToManyField(User)

    def __str__(self):
        return f"Project: {self.title}"


class Todo(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.CharField(max_length=64)
    text = models.TextField(max_length=512, blank=True)
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.todo} [{self.create_date}]"
