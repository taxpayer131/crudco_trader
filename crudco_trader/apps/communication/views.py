# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def create(request):
    return HttpResponse("process a create a comment request")
def read(request):
    return HttpResponse("view a list of comments")
def update(request):
    return HttpResponse("process a request to edit a comment")
def delete(request):
    return HttpResponse("process a request to delete a comment")