"""
   - Этот файл содержит представления (views) приложения, обрабатывающие запросы и формирующие ответы.
   - Функция start_page: рендерит главную страницу приложения.
   - Функция register: обрабатывает регистрацию пользователей. Проверяет форму, сохраняет данные нового пользователя и перенаправляет на главную страницу с сообщением об успехе.
   - Функция login_view: обрабатывает процесс входа пользователя. Проверяет форму и, если данные верны, выполняет вход. В случае ошибки выводит сообщение.
   - Функция send_message: обрабатывает отправку сообщений пользователями. Проверяет форму и сохраняет сообщение, если форма корректна.
   - Функция profile: отображает профиль пользователя и, если он авторизован, показывает его сообщения. Если пользователь не авторизован, возвращает пустой список сообщений.
"""

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegistrationForm, AuthorisationForm, MessageForm
from .models import Message


def start_page(request):
    return render(request, 'user/start_page.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Успешная регистрация!")
            return redirect('start_page')
    else:
        form = RegistrationForm()
    return render(request, 'user/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthorisationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Неправильные учетные данные.")
    else:
        form = AuthorisationForm()
    return render(request, 'user/login.html', {'form': form})


def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()
            messages.success(request, "Сообщение отправлено.")
            return redirect('send_message')
    else:
        form = MessageForm()
    return render(request, 'user/send_message.html', {'form': form})


def profile(request):
    if request.user.is_authenticated:
        messages = Message.objects.filter(user=request.user)
    else:
        messages = []  # Если пользователь не аутентифицирован, возвращаем пустой список
    return render(request, 'user/profile.html', {'messages': messages})
