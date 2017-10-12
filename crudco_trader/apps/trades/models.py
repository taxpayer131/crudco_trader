# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..users.models import User

class TradeManager(models.Manager):
    def creation_validator(self,postData):
        errors = {}
        if 'category' not in  postData:
            errors['category'] = "Category required"
        if postData['item'] == "other":
            if len(postData['other'])<1:
                errors ['item'] = "Item name required"
        if len(postData['item']) < 1:
            errors ['item'] = "Item name required"
        if len(postData['item']) < 3:
            errors ['item'] = "Item name too short"
        if len(postData['description']) < 1:
            errors['description'] = "Description required"
        if len(postData['description']) < 5:
            errors['description'] = "Description too short"
        return errors

# Create your models here.
class Trade(models.Model):
    originator = models.ForeignKey(User, related_name = "my_trades")
    recipient = models.ForeignKey(User, related_name = "trades", blank=True, null=True)
    item = models.CharField(max_length = 50)
    status = models.CharField(max_length = 50)
    category = models.CharField(max_length = 100)
    quantity = models.IntegerField()
    description = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = TradeManager()
