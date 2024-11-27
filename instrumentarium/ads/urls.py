from django.urls import path

from instrumentarium.ads.views import HomeView, AdBoardView, UploadAdView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('ads/', AdBoardView.as_view(), name='ad-board'),
    path('upload/', UploadAdView.as_view(), name='upload'),
]

