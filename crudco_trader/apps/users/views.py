# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("view the home page")
def login(request):
    return HttpResponse("login")
def new(request):
    return HttpResponse("view a new user page")
def create(request):
    return HttpResponse("create create create a user")
def profile(request):
    return HttpResponse("view some info about a user")
def edit(request):
    return HttpResponse("view a page to edit user profile")
def update(request):
    return HttpResponse("update the user db with new info")
def delete(request):
    return HttpResponse("delete your own account")
def logout(request):
    return HttpResponse("goodbye!")