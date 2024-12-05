from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from instrumentarium.ads.forms import UploadAdForm
from instrumentarium.ads.models import Ad, Like


class HomeView(TemplateView):
    template_name = 'common/base.html'


class AdBoardView(ListView):
    model = Ad
    template_name = 'ads/ad-board.html'
    context_object_name = 'ads'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            liked_ads = {ad.pk: ad.likes.filter(user=self.request.user).exists() for ad in context['ads']}
            context['liked_ads'] = liked_ads

        return context


class UploadAdView(LoginRequiredMixin, CreateView):
    form_class = UploadAdForm
    template_name = 'ads/ad-upload.html'
    success_url = reverse_lazy('ad-board')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required
def like_ad(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    Like.objects.get_or_create(user=request.user, ad=ad)
    return redirect('ad-board')


@login_required
def unlike_ad(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    like = Like.objects.filter(user=request.user, ad=ad)

    if like:
        like.delete()

    return redirect('ad-board')
