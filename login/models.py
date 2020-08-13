from django.db import models

# Create your models here.
from django.contrib.auth.models import User

#Email Field
User._meta.get_field('email')._unique = True
User._meta.get_field('email').blank = False
User._meta.get_field('email').null = False

#First_Name Field
User._meta.get_field('first_name').blank = False
User._meta.get_field('first_name').null = False

#Last_Name Field
User._meta.get_field('last_name').blank = False
User._meta.get_field('last_name').null = False