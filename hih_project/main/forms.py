from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Textarea, CharField, PasswordInput
from django.db.models import Model
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model: Model = Task
        fields = ["title", 'task']
        widgets = {
            "title": TextInput(attrs={
                'class':'frmc',
                'placeholder':'Введите название'
               }),
            "task": Textarea(attrs={
                'class':'frmc',
                'placeholder':'Введите название'
               }),
               }
        

class SignUpForm(UserCreationForm):
    class Meta:
        model: Model = User
        fields: tuple[str, ...] = 'username', 'password1', 'password2'


class LoginForm(AuthenticationForm):
    username: CharField = CharField(label='Имя пользователя')
    password: CharField = CharField(label='Пароль', widget=PasswordInput)
