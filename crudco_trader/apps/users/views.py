# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .forms import LoginForm, RegistrationForm
from .models import User
from ..communication.models import Review
from ..trades.models import Trade
import bcrypt

# Create your views here.
def index(request):
    if 'id' not in request.session:
        login = LoginForm()
        return render(request, 'users/login.html', {'form':login})
    else:
        return redirect('/trades/')
def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags = tag)
            return redirect('/')
    else:
        username = request.POST['username']
        temp = User.objects.get(username = username)
        request.session['id'] = temp.id
        return redirect('../trades/')
def new(request):
    if 'id' not in request.session:
        register = RegistrationForm()
        return render(request, 'users/register.html', {'form': register})
    else:
        return redirect('/trades/')
def create(request):
    errors = User.objects.registration_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags = tag)
        return redirect('/new')
    else:
        fname = request.POST['first']
        lname = request.POST['last']
        username = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['pwd']
        cpw = request.POST['cpw']
        zipcode = request.POST['zipcode']
        hash1 = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt())
        User.objects.create(first_name = fname, last_name = lname, username = username, zipcode = zipcode, email = email, password = hash1)
        temp = User.objects.get(username = username)
        request.session['id'] = temp.id
        return redirect('../trades/')
def profile(request, user_id):
    if 'id' not in request.session:
        return redirect('/')
    else:
        id = request.session['id']
        me = User.objects.get(id = id)
        user = User.objects.get(id = user_id)
        mytrades = Trade.objects.filter(originator = user)
        available = mytrades.filter(status = 'active')
        mypending = mytrades.filter(status = 'pending')
        completed = mytrades.filter(status = 'completed')
        pending = Trade.objects.filter(recipient = user)    
        pending = pending.filter(status = 'pending')
        reviews = Review.objects.filter(reviewee = user)
        context = {
            'user': me,
            'profile': user,
            'available': available,
            'mypending': mypending,
            'pending': pending,
            'completed': completed,
            'reviews': reviews,
        }
        return render(request, 'users/profile.html', context)
def edit(request):
    return HttpResponse("view a page to edit user profile..coming soon")
def update(request):
    return HttpResponse("update the user db with new info...ariving after the edit view")
def delete(request, user_id):
    return HttpResponse("delete your own account...ariving later than everything else...because...")
def logout(request):
    del request.session['id']
    return redirect('/')