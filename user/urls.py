"""
   - Этот файл содержит маршруты (URL-адреса) приложения, связывая URL-адреса с соответствующими представлениями.
   - Связывает URL-адреса с функциями представлений: start_page, register, login_view, send_message, profile.
"""
from django.urls import path
from .views import start_page, register, login_view, send_message, profile

urlpatterns = [
    path('', start_page, name='start_page'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('send_message/', send_message, name='send_message'),
    path('profile/', profile, name='profile'),
]