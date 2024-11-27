from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from instrumentarium.ads.forms import UploadAdForm
from instrumentarium.ads.models import Ad


class HomeView(TemplateView):
    template_name = 'common/base.html'


class AdBoardView(ListView):
    model = Ad
    template_name = 'ads/ad-board.html'
    context_object_name = 'ads'


class UploadAdView(CreateView):
    form_class = UploadAdForm
    template_name = 'ads/ad-upload.html'
    success_url = reverse_lazy('ad-board')
