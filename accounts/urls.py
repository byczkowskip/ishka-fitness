from django.conf import settings
from django.urls import path
from django.contrib.auth import views as auth_views

from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.AccountLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('reset-password/', views.AccountPasswordResetView.as_view(), name='reset_password'),
    path('reset-password/confirm/<uidb64>/<token>/', views.AccountPasswordResetConfirmView.as_view(), name='reset_password_confirm'),
    path('reset-password/done/', views.AccountPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('register/', views.AccountRegisterFormView.as_view(), name='register'),
    path('settings/', views.AccountSettingFormView.as_view(), name='settings'),
]