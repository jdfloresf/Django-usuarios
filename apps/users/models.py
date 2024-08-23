from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    """Model definition for User."""

    GENDER = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    )

    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField(max_length=254)
    nombres = models.CharField(max_length=20, blank=True)
    apellidos = models.CharField(max_length=20, blank=True)
    genero = models.CharField(max_length=1, choices=GENDER, blank=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    class Meta:
        """Meta definition for User."""

        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_short_name(self):
        return self.username
    
    def get_full_name(self):
        return self.nombres + self.apellidos

    def __str__(self):
        """Unicode representation of User."""
        return int(self.id) + '-' + self.nombres
