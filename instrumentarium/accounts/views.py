from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from instrumentarium.accounts.forms import CustomUserCreationForm, ProfileUpdateForm
from instrumentarium.accounts.models import Profile

User = get_user_model()


class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')


class ProfileLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return self.success_url


def logout_confirm_view(request):
    return render(request, template_name='registration/logout-confirm.html')


class UserDetailsView(DetailView):
    model = User
    template_name = 'users/user-details.html'


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'users/profile-update.html'

    def get_success_url(self):
        return reverse_lazy('user-details', kwargs={'pk': self.object.user.pk})

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)


@login_required
@permission_required('accounts.can_deactivate_accounts', raise_exception=True)
def activate_account(request, pk):
    account = get_object_or_404(User, pk=pk)
    account.is_active = True
    account.save()

    return redirect('user-details', pk=pk)


@login_required
@permission_required('accounts.can_deactivate_accounts', raise_exception=True)
def deactivate_account(request, pk):
    account = get_object_or_404(User, pk=pk)
    if account == request.user:
        raise ValueError("You cannot deactivate your own account!")
    if account.is_superuser:
        raise ValueError("You cannot deactivate superuser account!")

    account.is_active = False

    ads = account.ads.all()
    for ad in ads:
        ad.is_active = False
        ad.save()

    account.save()

    return redirect('user-details', pk=pk)


def uploaded_ads_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    ads = user.ads.all()

    context = {
        'user': user,
        'ads': ads
    }

    return render(request, 'users/user-ads.html', context=context)


def liked_ads_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    like_ads = user.likes.select_related('ad').all()

    context = {
        'user': user,
        'like_ads': like_ads
    }

    return render(request, 'users/user-liked-ads.html', context=context)
