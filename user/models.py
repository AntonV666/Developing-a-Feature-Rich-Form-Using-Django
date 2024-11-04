"""
  - Этот файл содержит модели базы данных для приложения.
   - Класс Message
     - user: связь с моделью User, представляет пользователя, который отправил сообщение.
     - email: адрес электронной почты отправителя сообщения.
     - text: текст сообщения, максимальная длина — 500 символов.
     - Метод __str__: возвращает строковое представление объекта, отображая адрес электронной почты отправителя.
"""

from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    text = models.TextField(max_length=500)

    def __str__(self):
        return f'Message from {self.email}'
