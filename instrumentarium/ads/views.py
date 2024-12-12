from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView

from instrumentarium.ads.forms import UploadAdForm, MessageForm, AddUpdateForm
from instrumentarium.ads.models import Ad, Like, Chat


class HomeView(TemplateView):
    template_name = 'common/base.html'


class AdBoardView(ListView):
    model = Ad
    template_name = 'ads/ad-board.html'
    context_object_name = 'ads'
    paginate_by = 6

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
@permission_required('ads.can_approve_ads', raise_exception=True)
def activate_ad(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    ad.is_active = True
    ad.save()

    return redirect('ad-detail', pk=pk)


@login_required
@permission_required('ads.can_approve_ads', raise_exception=True)
def deactivate_ad(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    ad.is_active = False
    ad.save()

    return redirect('ad-detail', pk=pk)


class DetailAdView(DetailView):
    model = Ad
    template_name = 'ads/ad-detail.html'


class UpdateAdView(UpdateView):
    model = Ad
    form_class = AddUpdateForm
    template_name = 'ads/ad-update.html'

    def get_success_url(self):
        return reverse_lazy('ad-detail', kwargs={'pk': self.object.pk})


# This view works for chats opened from the ad-detail page
@login_required
def start_chat(request, pk):
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
            return redirect('chat-initial', pk=ad.pk)
    else:
        form = MessageForm(initial={'content': ''})

    context = {
        'ad': ad,
        'chat': chat,
        'form': form,
    }

    return render(request, template_name='chats/ad-chat.html', context=context)


# This view works for chats opened from the user-chats page
def continue_chat(request, chat_pk):
    chat = get_object_or_404(Chat, pk=chat_pk)

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.chat = chat
            message.save()
            return redirect('chat', chat_pk=chat.pk)
    else:
        form = MessageForm(initial={'content': ''})

    context = {
        'ad': chat.ad,
        'chat': chat,
        'form': form,
    }

    return render(request, template_name='chats/ad-chat.html', context=context)


class ChatDetailView(ListView):
    model = Chat
    template_name = 'chats/user-chats.html'
    context_object_name = 'chats'

    def get_queryset(self):
        queryset = Chat.objects.filter(
            Q(user1=self.request.user) | Q(user2=self.request.user)
        )

        return queryset

