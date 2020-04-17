"""auth_app URL Configuration"""
from django.urls import path
import auth_app.views as auth_app

app_name = 'auth_app'
urlpatterns = [
    path('', auth_app.main, name='main'),
    path('login', auth_app.login, name='login'),
    path('info', auth_app.info, name='info'),
    path('logout', auth_app.logout, name='logout'),
]
