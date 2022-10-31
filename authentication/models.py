from django.contrib.auth.models import AbstractUser, Group
from django.db import models


class User(AbstractUser):
    rut = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = 'users'


TOKEN_TYPES = (
    ('reset_password', 'reset_password'),
    ('activation', 'activation'),
)


class Token(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    type = models.CharField(max_length=15, default=TOKEN_TYPES[1][0])

    class Meta:
        db_table = 'tokens'
