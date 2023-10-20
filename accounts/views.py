from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import LoginForm, UserEditForm
from django.views.generic.base import View


# Create your views here.
def login_user(request):
    if request.user.is_authenticated:
        return redirect('home:home')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect('home:home')
    else:
        form = LoginForm
    return render(request, 'accounts/login.html', {'form': form})


def register_user(request):
    context = {'errors': []}
    if request.user.is_authenticated:
        return redirect('home:home')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            context['errors'].append('passwords are not same')
            return render(request, 'accounts/register.html', context)

        user = User.objects.create(username=username, password=password1, email=email)
        login(request, user)
        return redirect('home:home')

    return render(request, 'accounts/register.html')


def edit_user(request):
    user = request.user
    form = UserEditForm(instance=user)
    if request.method == "POST":
        form = UserEditForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'accounts/edit.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('home:home')
