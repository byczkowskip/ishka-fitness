from typing import Any

from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from accounts.forms import AccountCreationForm, AccountPasswordResetForm, AccountAuthenticationForm, \
    AccountUserUpdateForm, AccountUserPasswordUpdateForm


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


class AccountSettingFormView(LoginRequiredMixin, FormView, SuccessMessageMixin):
    template_name = 'accounts/settings_form.html'
    success_url = reverse_lazy('accounts:settings')
    success_message = ''

    def get_initial(self):
        initial = super().get_initial()
        return initial

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super(AccountSettingFormView, self).get_context_data(**kwargs)
        context['user_form'] = self.get_user_form()
        context['password_form'] = self.get_password_form()
        return context

    def get_user_form(self):
        if self.request.POST:
            return AccountUserUpdateForm(self.request.POST, instance=self.request.user)
        else:
            return AccountUserUpdateForm(instance=self.request.user)

    def get_password_form(self):
        if self.request.POST:
            return AccountUserPasswordUpdateForm(self.request.user, self.request.POST)
        else:
            return AccountUserPasswordUpdateForm(self.request.user)

    def form_valid(self, form):
        user_form = self.get_user_form()
        password_form = self.get_password_form()
        forms_valid = True

        if user_form.is_valid():
            user_form.save()
        else:
            forms_valid = False

        if len(password_form.changed_data):
            if password_form.is_valid():
                password_form.save()
            else:
                forms_valid = False

        if not forms_valid:
            return self.form_invalid(form)

        return super().form_valid(form)

    def get_form(self, form_class=None):
        if form_class is None or form_class == AccountUserUpdateForm:
            return self.get_user_form()
        return super().get_form(form_class)

