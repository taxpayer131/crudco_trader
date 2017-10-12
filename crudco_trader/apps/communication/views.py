# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse, reverse
from .models import Comment, CommentManager
from ..trades.models import Trade
from ..users.models import User

# Create your views here.
def create(request, trade_id):
    id = trade_id
    print request.POST['comment']
    trade = Trade.objects.get(id = trade_id)
    user = User.objects.get(id = request.session['id'])
    comment = request.POST['comment']
    Comment.objects.create(commentator = user, trade = trade, comment = comment)
    return redirect(reverse('trades:show', kwargs={ 'trade_id': id }))
def read(request, message_id):
    message = Comment.objects.get(id = message_id)
    trade = message.trade
    conversation = Comment.objects.include(trade = trade)
    context = {
        'message_id': message_id,
        'conversation': conversation,
    }
    return render(request, 'communication/edit.html', context)
def update(request):
    return HttpResponse("process a request to edit a comment")
def delete(request):
    return HttpResponse("process a request to delete a comment")