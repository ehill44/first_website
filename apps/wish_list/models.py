from __future__ import unicode_literals
from django.db import models
from ..startpage.models import *
from datetime import datetime, timedelta

class ProductManager(models.Manager):
    def validator(self,postData):
        errors2= {}
        if len(postData['item'])<=1:
            errors2['item'] = "You cannot submit an empty entry"
        return errors2


class Product(models.Model):
    item = models.CharField(max_length=45)
    added_by = models.ForeignKey(User, related_name='adder')
    date_added= models.DateField(auto_now_add=True)
    others = models.ManyToManyField(User, related_name='also_wants')
    objects=ProductManager()


