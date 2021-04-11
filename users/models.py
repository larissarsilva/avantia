from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = models.CharField(max_length=15, verbose_name = "Primeiro Nome" )
    last_name = models.CharField(max_length=15, verbose_name = "Último Nome" )
    username = models.CharField(unique = True, max_length=15, verbose_name = "Usuário" )
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
