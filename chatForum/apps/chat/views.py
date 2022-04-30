from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.sessions.models import Session

from django.contrib.auth.decorators import login_required
from channels.db import database_sync_to_async
from asgiref.sync import sync_to_async

from .models import Forum, Message
from accounts.models import User
from .forms import CreateForumForm

# Create your views here.

@login_required
def index(request):
    if request.method == 'POST':
        request.user.has_logged_in = False
        request.user.save()
        logout(request)
        return redirect('login')
    
    return render(request, 'index.html', {
        'username': request.user.username,
        'image': request.user.image,
    })


@login_required
def enter_forum(request):
    if request.method == 'POST':
        forum_name = request.POST.get('name')
        try:
            forum = Forum.objects.get(name = forum_name)
            if forum:
                if request.user not in forum.participants.all():
                    forum.participants.add(request.user)
                return HttpResponseRedirect('/chat/' + forum_name + '/?username=' + request.user.username)
        except Forum.DoesNotExist:
            messages.error(request, 'Looks like the forum {} does not exist.'.format(forum_name))
    return render(request, 'enter_forum.html')

@login_required
def create_forum(request):
    form = CreateForumForm()
    if request.method == 'POST':
        form = CreateForumForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                forum = Forum.objects.get(name = form.cleaned_data.get('name'))
                if forum:
                    messages.error(request, 'Looks like the forum {} already exists.'.format(form.cleaned_data.get('name')))
            except Forum.DoesNotExist:
                forum = Forum.objects.create(admin = request.user.username, name = form.cleaned_data.get('name'), image = form.cleaned_data.get('image'), description = form.cleaned_data.get('description'))
                forum.participants.add(request.user)
                forum.save()
                request.session['forum'] = form.cleaned_data.get('name')
                return redirect('success_forum')

    return render(request, 'create_forum.html', {
        'form': form
    })


@login_required
def room(request, room_name):
    username = request.user.username
    messages = Message.objects.filter(room = Forum.objects.get(name = room_name))[0:25]

    return render(request, 'room.html', {
        'room': Forum.objects.get(name = room_name),
        'user': User.objects.get(username = username),
        'messages': messages
    })


@login_required
def success_forum(request):
    name = request.session['forum']

    return render(request, 'success_forum.html', {
        'ForumName' : name
    })