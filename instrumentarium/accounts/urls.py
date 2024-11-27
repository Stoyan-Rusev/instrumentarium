from django.contrib.auth.views import LogoutView
from django.urls import path, include

from instrumentarium.accounts.views import ProfileLoginView, logout_confirm_view, UserRegisterView, UserDetailsView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', ProfileLoginView.as_view(), name='login'),
    path('logout-confirmation/', logout_confirm_view, name='logout-confirmation'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<int:pk>/', include([
        path('details/', UserDetailsView.as_view(), name='user-details'),
    ])),
]
