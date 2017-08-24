# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import UserProfile
from django.contrib.auth import authenticate, login, get_user_model, logout
from forms import *
from django.views.generic import View
from django.contrib import messages


def index(request):
    return render(request, 'game/index.html')

class UserFormView(View):
    form_class = UserForm
    template_name = 'game/registration.html'

    # display new user form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    #add new user to database
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            #format input data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            #authenticate user
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('poker:index')
        return render(request, self.template_name, {'form': form})


def login_view(request):
    form = UserLoginForm(request.POST)
    print(request.user.is_authenticated())
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request,user)
            print(request.user.is_authenticated())
            return redirect('poker:profile')
        else:
            return render(request, 'game/login.html', {'form': form, 'context': 'Username and password do not match'})
    else:
        return render(request, 'game/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'game/logout.html')


@login_required(login_url='/login/')
def profile(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('poker:profile')
    else:
        form = CreateProfileForm(instance=profile)
    return render(request, 'game/profile.html', {"form":form,'user':request.user})


@login_required(login_url='/login/')
def game(request):
    return render(request, 'game/game.html', {'user':request.user})


