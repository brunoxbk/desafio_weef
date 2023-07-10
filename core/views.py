from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from core.forms import UserForm, LoginForm
from django.urls import reverse_lazy


class UserCreate(CreateView):
    form_class = UserForm
    template_name = 'auth/signup.html'
    success_url = reverse_lazy('login')


class CustomLogin(LoginView):
    template_name = 'auth/login.html'
    form_class = LoginForm
