"""auth_app URL Configuration."""
from django.urls import path

from emphasoft.auth_app import views as auth_app_views

app_name = 'auth_app'
urlpatterns = [
    path('', auth_app_views.main, name='main'),
    path('login', auth_app_views.login, name='login'),
    path('info', auth_app_views.info, name='info'),
    path('logout', auth_app_views.logout, name='logout'),
]
