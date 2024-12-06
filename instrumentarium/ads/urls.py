from django.urls import path, include

from instrumentarium.ads.views import HomeView, AdBoardView, UploadAdView, like_ad, unlike_ad, DetailAdView, \
    chat_view

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('ads/', include([
        path('', AdBoardView.as_view(), name='ad-board'),
        path('upload/', UploadAdView.as_view(), name='upload'),
        path('<int:pk>/', include([
            path('like/', like_ad, name='ad-like'),
            path('unlike/', unlike_ad, name='ad-unlike'),
            path('detail/', DetailAdView.as_view(), name='ad-detail'),
            path('chat/', chat_view, name='chat'),
        ])),
    ])),
]
