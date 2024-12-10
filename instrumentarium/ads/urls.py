from django.urls import path, include

from instrumentarium.ads.views import HomeView, AdBoardView, UploadAdView, like_ad, unlike_ad, DetailAdView, \
    activate_ad, deactivate_ad, start_chat

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('ads/', include([
        path('', AdBoardView.as_view(), name='ad-board'),
        path('upload/', UploadAdView.as_view(), name='upload'),
        path('<int:pk>/', include([
            path('like/', like_ad, name='ad-like'),
            path('unlike/', unlike_ad, name='ad-unlike'),
            path('activate/', activate_ad, name='ad-activate'),
            path('deactivate/', deactivate_ad, name='ad-deactivate'),
            path('detail/', DetailAdView.as_view(), name='ad-detail'),
            path('chat/', start_chat, name='chat-initial'),
        ])),
    ])),
]
