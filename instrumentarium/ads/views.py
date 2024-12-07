from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView

from instrumentarium.ads.forms import UploadAdForm, MessageForm
from instrumentarium.ads.models import Ad, Like, Chat


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

    def get_queryset(self):
        queryset = self.model.objects.all()

        if not self.request.user.has_perm('ads.can_approve_ads'):
            queryset = self.model.objects.filter(is_active=True)

        return queryset


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
    next_url = request.GET.get('next')
    return redirect(next_url if next_url else 'ad-board')


@login_required
def unlike_ad(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    like = Like.objects.filter(user=request.user, ad=ad)

    if like:
        like.delete()

    next_url = request.GET.get('next')
    return redirect(next_url if next_url else 'ad-board')


@login_required
def activate_ad(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    ad.is_active = True
    ad.save()

    return redirect('ad-detail', pk=pk)


@login_required
def deactivate_ad(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    ad.is_active = False
    ad.save()

    return redirect('ad-detail', pk=pk)


class DetailAdView(DetailView):
    model = Ad
    template_name = 'ads/ad-detail.html'


@login_required
def chat_view(request, pk):
    ad = get_object_or_404(Ad, pk=pk)

    # Sorting the users, because of the 'save' method in Chat model
    user1, user2 = sorted([request.user, ad.author], key=lambda user: user.id)
    chat, created = Chat.objects.get_or_create(ad=ad, user1=user1, user2=user2)

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.chat = chat
            message.save()
            return redirect('chat', pk=ad.pk)
    else:
        form = MessageForm(initial={'content': ''})

    context = {
        'ad': ad,
        'chat': chat,
        'form': form,
    }

    return render(request, template_name='chats/ad-chat.html', context=context)

