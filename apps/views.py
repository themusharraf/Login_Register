from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from apps.forms import UserForm
from apps.models import Users


class IndexView(TemplateView):
    template_name = 'index.html'


class CustomLoginView(LoginView):
    next_page = '/index'
    redirect_authenticated_user = True
    template_name = 'login.html'
    success_url = reverse_lazy('index')


class RegisterView(CreateView):
    model = Users
    form_class = UserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

