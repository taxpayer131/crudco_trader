# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class TradeManager(models.Manager):
    def creation_validator(self,postData):
        errors = {}
        return errors

# Create your models here.
class Trade(models.Model):
    originator = models.ForeignKey('users.User', related_name = "my_trades")
    recipient = models.ForeignKey('users.User', related_name = "trades")
    item = models.CharField(max_length = 50)
    status = models.IntegerField(max_length = 5)
    category = models.CharField(max_length = 100)
    description = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = TradeManager()