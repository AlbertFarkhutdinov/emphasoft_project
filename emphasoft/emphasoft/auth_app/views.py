"""Views for auth_app"""
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse


def main(request):
    """View for rendering of main page"""
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('auth:info'))
    return HttpResponseRedirect(reverse('auth:login'))


def login(request):
    """View for rendering of login page"""
    if request.method == 'POST':
        post_data = request.POST
        username = post_data.get('username')
        password = post_data.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            user.save()
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return HttpResponseRedirect(reverse('auth:info'))

    get_next = request.GET.get('next')
    context = {
        'title': 'Вход',
        'next': get_next,
    }
    return render(request, 'auth_app/login.html', context)


def info(request):
    """View for rendering of info page"""
    friends = request.user.customuserprofile.friends
    friends = friends.split(',') if friends else None
    context = {
        'title': 'Информация о пользователе',
        'friends': friends,
    }
    return render(request, 'auth_app/info.html', context)


def logout(request):
    """View for rendering of logout"""
    auth.logout(request)
    return HttpResponseRedirect(reverse('auth:login'))
