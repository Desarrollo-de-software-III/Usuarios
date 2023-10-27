from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.conf import settings

# Create your models here.
# class user(models.Model):
    # usuario = models.CharField()
    # email = models.EmailField()
    # nombres = models.CharField()
    # apellidos = models.CharField()

class Usuario(AbstractUser):
    seguidores = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='seguidoresII', default="")
    siguiendo = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='siguiendoII', default="")
    # Otros campos específicos de tu modelo

    def __str__(self):
        return self.nombre

