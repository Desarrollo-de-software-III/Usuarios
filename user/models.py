from django.db import models
from datetime import date
# Create your models here.
class User(models.Model):
    """

    """
    email = models.EmailField(
        max_length=255,
        unique=True,
        primary_key=True
    )
    date_of_birth = models.DateField(null=True)
    date_of_creation = models.DateField(default=date.today())
    username = models.CharField(max_length=64, default="Q_user",null=False, blank=False)
    user_description = models.TextField(max_length=5000, null=True, blank=True)
    followed_users = models.ManyToManyField('self', blank=True, symmetrical=False)
    profile_photo_url = models.URLField(null=True, default=None)
    def __str__(self):
        return self.username
