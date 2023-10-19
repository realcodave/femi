from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField(verbose_name='phone_number', max_length=30)
    account_type = models.CharField(verbose_name='account', max_length=30)