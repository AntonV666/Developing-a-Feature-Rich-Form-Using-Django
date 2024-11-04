"""
   - Этот файл содержит формы для регистрации, авторизации и отправки сообщений.
   - Класс RegistrationForm: форма для регистрации пользователей. Содержит поля для имени пользователя, email и паролей.
   - Класс AuthorisationForm: форма для авторизации пользователей. Содержит поля для имени пользователя и пароля.
   - Класс MessageForm: форма для отправки сообщений. Проверяет, что текст сообщения не пустой и не превышает 500 символов.
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Message


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class AuthorisationForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('email', 'text')

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if not text or len(text) > 500:
            raise forms.ValidationError("Сообщение не может быть пустым и должно содержать не более 500 символов.")
        return text
