from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

User


class Kierownicy(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
