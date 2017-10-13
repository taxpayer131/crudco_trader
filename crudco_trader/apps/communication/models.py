# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class CommentManager(models.Manager):
    def creation_validator(self,postData):
        errors = {}
        if len(postData['comment']) < 1:
            errors['comment'] = "Missing comment"
        return errors
class ReviewManager(models.Manager):
    def review_validator(self,postData):
        errors = {}
        if len(postData['review'])<1:
            errors['review'] = 'Review missing'
        return errors        

# Create your models here.
class Comment(models.Model):
    commentator = models.ForeignKey('users.User', related_name = "comments")
    trade = models.ForeignKey('trades.Trade', related_name = "comments")
    comment = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CommentManager()

class Review(models.Model):
    stars = models.IntegerField()
    review = models.CharField(max_length = 255)
    reviewer = models.ForeignKey('users.User', related_name = 'critiques')
    reviewee = models.ForeignKey('users.User', related_name = 'reviews')
    trade = models.ForeignKey('trades.Trade', related_name = 'reviews')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ReviewManager()