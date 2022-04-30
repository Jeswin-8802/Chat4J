from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from .forms import RegistrationForm, LoginForm, Profile
from django.contrib import messages
from .models import User
from django.contrib.sessions.models import Session

# Create your views here.

def login(request):
    if request.method == 'POST':    
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user:
                if user.has_logged_in:
                    messages.error(request, 'Looks like you\'ve already logged in!')
                else:
                    user.has_logged_in = True
                    user.save()
                    auth_login(request, user)
                    return redirect('index')
            else:
                messages.error(request, 'Please enter a correct username and password. Note that both fields may be case-sensitive.')
    return render(request, 'login.html')

def signup(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['username'] = form.cleaned_data.get('username')
            return redirect('upload')
    return render(request, 'signup.html', {
        'form' : form
    })

def success(request):
    return render(request, 'success.html')

def upload(request):
    if request.method == 'POST':
        form = Profile(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.get(username = request.session['username'])
            user.image = form.cleaned_data.get('image')
            user.bio = form.cleaned_data.get('bio')
            user.save()
            Session.objects.all().delete()
            return redirect('success')
    else:
        form = Profile()
    return render(request, 'profile.html', {'form': form})