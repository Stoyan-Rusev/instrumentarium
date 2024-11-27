from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from instrumentarium.accounts.forms import CustomUserCreationForm
from instrumentarium.accounts.models import Profile, User


class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')


class ProfileLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return self.success_url


class UserDetailsView(DetailView):
    model = User
    template_name = 'users/user-details.html'


def logout_confirm_view(request):
    return render(request, template_name='registration/logout-confirm.html')
