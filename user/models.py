from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.
# class user(models.Model):
    # usuario = models.CharField()
    # contraseña=models.CharField()
    # email = models.EmailField()
    # nombres = models.CharField()
    # apellidos = models.CharField()

class Usuario(models.Model):
    seguidores = models.ManyToManyField(User,related_name='seguidores')
    siguiendo = models.ManyToManyField(User,related_name='siguiendo')
    # Otros campos específicos de tu modelo

    def __str__(self):
        return self.nombre

