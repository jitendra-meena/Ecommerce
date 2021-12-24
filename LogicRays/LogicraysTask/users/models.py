from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.validators import RegexValidator

from .managers import CustomUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(('email address'), unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,17}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True, unique = True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']
    profile_pic = models.ImageField(upload_to='media', blank=True, null=False)
    
    objects = CustomUserManager()

    def __str__(self):
        return self.email
        