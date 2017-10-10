# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from ..users.models import User
from .models import Trade
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def add(request):
    return render(request, 'trades/new.html')
def create(request):
    errors = Trade.objects.creation_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/trades/add')
    else:
        originator = User.objects.get(id = request.session['id'])
        print originator.first_name
        item = request.POST['item']
        status = 'active'
        category = request.POST['category']
        description = request.POST['description']
        quantity = request.POST['quantity']
        Trade.objects.create(originator = originator, item = item, status = status, category = category, description = description, quantity = quantity)
        return redirect('/trades/')
    return HttpResponse("process adding a new form")
def edit(request):
    return HttpResponse("view a page to edit trade info/status")
def update(request):
    return HttpResponse("process/submit updated trade info")
def delete(request):
    return HttpResponse("delete a trade")
def read(request):
    user = User.objects.get(id = request.session['id'])
    print user.first_name
    trades = Trade.objects.filter(status = 'active')
    trades = trades.exclude(originator = user)
    print trades.first().item
    context = {
        'trades': trades,
        'user': user
    }
    return render(request, 'trades/dashboard.html', context = context)
    return HttpResponse("view trade details")