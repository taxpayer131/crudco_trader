# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def add(request):
    return render(request, 'trades/new.html')
def create(request):
    return HttpResponse("process adding a new form")
def edit(request):
    return HttpResponse("view a page to edit trade info/status")
def update(request):
    return HttpResponse("process/submit updated trade info")
def delete(request):
    return HttpResponse("delete a trade")
def read(request):
    return HttpResponse("view trade details")