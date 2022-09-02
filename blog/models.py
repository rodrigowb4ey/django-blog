from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    uuid = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class News(models.Model):
    uuid = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
