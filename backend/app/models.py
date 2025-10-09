from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import only_numbers, valid_cpf, valid_phone, valid_zipcode


class Users(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=True, null=True, validators=[only_numbers, valid_cpf])
    phone = models.CharField(max_length=11, blank=True, null=True, validators=[only_numbers, valid_phone])
    date_birth = models.DateField(blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    number = models.CharField(max_length=25, blank=True, null=True)
    complement = models.CharField(max_length=200, blank=True, null=True)
    neighborhood = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=8, blank=True, null=True, validators=[only_numbers, valid_zipcode])
    observations = models.TextField(blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
