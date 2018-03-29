from __future__ import unicode_literals
from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta

class UserManager(models.Manager):
    def basic_validator(self,postData):
        errors= {}
        if len(postData['first_name'])<=2 or not postData['first_name'].isalpha():
            errors['first_name'] = "User's first name needs more than 2 characters"

        if len(postData['user_name'])<=2:
            errors['user_name'] = "Username needs more than 2 characters"
        
        password_conf = postData['confpass']
        if len(postData['password'])<=8 or postData['password'] != password_conf :
            errors['password'] = "Password must be greater than 8 characters"
        return errors
 

class User(models.Model):
    first_name = models.CharField(max_length=15)
    user_name = models.CharField(max_length=15)
    password = models.CharField(max_length=25)
    date_hired = models.DateField()
    objects = UserManager()
