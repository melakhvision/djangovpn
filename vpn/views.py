import os
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from vpn.script.function import revoke_profile, create_profile, enable_scripts
from django.conf import settings
from vpn.models import Profile
import psutil


def dashboard(request):
    # redirect to login page if user is not authenticated
    if not request.user.is_authenticated:
        return redirect('index')
    context = {}
    query = Profile.objects.all()
    context['profiles'] = query
    if request.method == 'GET':
        cpu_load = psutil.cpu_percent()
        get_ram_usage = psutil.virtual_memory().percent
        context["URL"] = f'http://{settings.DOMAIN}/media/'
        context['cpu_load'] = cpu_load
        context['ram_usage'] = get_ram_usage
        return render(request, 'dashboard.html', context)
    if request.method == 'POST':
        name = request.POST['username']
        query = Profile.objects.filter(name=name)
        if query:
            context['error'] = 'User already exists'
            return redirect(request, 'dashboard.html', context)
        else:
            error = create_profile(name)
            if error is not None:
                context['error'] = "couldn't create a profile an error occured"
                return render(request, 'dashboard.html', context)
            Profile.objects.create(name=name)
            context['success'] = 'User created successfully'
            context["URL"] = f'http://{settings.DOMAIN}/media/'
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
    if not request.user.is_authenticated:
        return redirect('index')
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


def server_status(request):
    # Replace this with your actual logic to get the server status
    cpu_load = psutil.cpu_percent()
    get_ram_usage = psutil.virtual_memory().percent
    return render(request, 'server_status.html', {'cpu_load': cpu_load, 'ram_usage': get_ram_usage})
