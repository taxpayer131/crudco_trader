# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def add(request):
    return HttpResponse("We are getting ready to add some trades...")