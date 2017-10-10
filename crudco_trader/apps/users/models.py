# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def registration_validator(self,postData):
        errors = {}
        #!!!!!Check if user already exists!!!
        emailsearch = User.objects.filter(email = postData['email'])
        if len(emailsearch)>0:
            errors['account'] = 'Account already exists'
        usersearch = User.objects.filter(username = postData['username'])
        if len(usersearch)>0:
            errors['account'] = 'Account already exists'
        #ensure first and last name contain only letters
        if not re.match(r'^[a-zA-Z]+$', postData['first']):
            errors['first'] = 'First name can only contain letters'
        if not re.match(r'^[a-zA-Z]+$', postData['last']):
            errors['last'] = 'Last name can only contain letters'
        #check if first name is at least one character long
        if len(postData['first'])<1:
            errors['first'] = "First name required"
        #check that passwords match
        if len(postData['pwd']) < 8:
            errors['password_length'] = "Passwords must be at least 8 characters long"
        if postData['pwd'] != postData['cpw']:
            errors['password'] = "Confirmation did not match password"
        #check if last name is at least two characters long
        if len(postData['last'])<2:
            errors['last'] = "Last name too short"
        if len(postData['last'])<1:
            errors['last'] = "Last name required"
        return errors
    def update_validator(self,postData):
        errors = {}
        #!!!!!Check if user already exists!!!
        #ensure first and last name contain only letters
        if not re.match(r'^[a-zA-Z]+$', postData['first']):
            errors['first'] = 'First name can only contain letters'
        if not re.match(r'^[a-zA-Z]+$', postData['last']):
            errors['last'] = 'Last name can only contain letters'
        #check if first name is at least one character long
        if len(postData['first'])<1:
            errors['first'] = "First name required"
        #check if last name is at least two characters long
        if len(postData['last'])<1:
            errors['last'] = "Last name required"
        elif len(postData['last'])<2:
            errors['last'] = "Last name too short"
        #check that passwords match
        if postData['pwd'] != postData['cpw']:
            errors['password'] = "Confirmation did not match password"
        if postData['pwd'] < 8 and postData['pwd'] > 0:
            errors['password'] = "Passwords must be at least 8 characters long"
        return errors
    def login_validator(self,postData):
        errors = {}
        #check if user exists
        username = postData['username']
        usersearch = User.objects.filter(username = username)
        if len(usersearch) < 1:
            errors['user']='User not found'
        #verify password
        else:
            pwd = postData['pwd']
            temp = User.objects.get(username = username)
            hashedpw = temp.password
            if not bcrypt.checkpw(pwd.encode(), hashedpw.encode()):
                errors['password']='Unable to authenticate'
        return errors

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    zipcode = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()