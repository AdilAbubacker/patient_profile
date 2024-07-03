from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
