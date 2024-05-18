import os
import pprint
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from vpn.script.function import list_dir, revoke_profile, create_profile
from django.conf import settings
from vpn.models import Profile


def dashboard(request):
    # redirect to login page if user is not authenticated
    context = {}
    query = Profile.objects.all()
    context['profiles'] = query
    if request.method == 'GET':
        # for dir in list_dir():
        #     print(dir)
        # print('\n'.join(map(str, list_dir())))
        context["URL"] = f'http://{settings.DOMAIN}/media/'
        if not request.user.is_authenticated:
            return redirect('index')
        return render(request, 'dashboard.html', context)
    if request.method == 'POST':
        name = request.POST['username']
        query = Profile.objects.filter(name=name)
        if query:
            context['error'] = 'User already exists'
            return render(request, 'dashboard.html', context)
        else:
            create_profile(1, name)
            Profile.objects.create(name=name)
            context['success'] = 'User created successfully'
            return render(request, 'dashboard.html', context)


def index(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            context['error'] = 'Login failed'
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('index')


def delete(request, id):
    context = {}
    name = Profile.objects.get(id=id).name
    if os.path.exists(f'/root/{name}.ovpn'):
        try:
            revoke_profile(name)
            Profile.objects.filter(id=id).delete()
            redirect('dashboard')
        except Exception as e:
            context['error'] = 'Error deleting profile'
            return redirect('dashboard', context)
    Profile.objects.filter(id=id).delete()
    return redirect('dashboard')
