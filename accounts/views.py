from typing import Any

from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from accounts.forms import AccountCreationForm, AccountPasswordResetForm, AccountAuthenticationForm


class AccountLoginView(LoginView):
    form_class = AccountAuthenticationForm
    template_name = 'accounts/login.html'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super(AccountLoginView, self).get_context_data(**kwargs)
        context['google_client_id'] = settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
        return context


class AccountPasswordResetView(PasswordResetView):
    form_class = AccountPasswordResetForm
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    success_url = reverse_lazy('accounts:password_reset_done')


class AccountPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'

class AccountPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'


class AccountRegisterFormView(FormView):
    form_class = AccountCreationForm
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('')
