from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path, include, reverse_lazy

from instrumentarium.accounts.views import ProfileLoginView, logout_confirm_view, UserRegisterView, UserDetailsView, \
    ProfileUpdateView, activate_account, deactivate_account, uploaded_ads_view, liked_ads_view
from instrumentarium.ads.views import ChatDetailView, continue_chat

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', ProfileLoginView.as_view(), name='login'),
    path('logout-confirmation/', logout_confirm_view, name='logout-confirmation'),
    path('password-change/', PasswordChangeView.as_view(
        template_name='registration/password_change.html', success_url=reverse_lazy('password-change-done')
    ), name='password-change', ),
    path('password-change-done/', PasswordChangeDoneView.as_view(
        template_name='registration/password_change_done.html'
    ), name='password-change-done'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<int:pk>/', include([
        path('details/', UserDetailsView.as_view(), name='user-details'),
        path('update/', ProfileUpdateView.as_view(), name='profile-update'),
        path('activate/', activate_account, name='account-activate'),
        path('deactivate/', deactivate_account, name='account-deactivate'),
        path('chats/', ChatDetailView.as_view(), name='user-chats'),
        path('uploaded_ads/', uploaded_ads_view, name='user-uploaded-ads'),
        path('liked-ads/', liked_ads_view, name='user-liked-ads'),
    ])),
    path('<int:chat_pk>/chat/', continue_chat, name='chat'),
]
