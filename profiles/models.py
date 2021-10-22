from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatar', default='no_picture.png')
    telephone_number = models.CharField(default='+375', max_length=13)

    def __str__(self):
        return f'Profile of {self.user.username}'
