from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class AccountAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        required=True,
        label=_('Email'),
        widget=forms.EmailInput(attrs={'name': 'email', 'autofocus': True}),
        error_messages={'required': 'Email address is required.', 'invalid': 'Enter a valid email address.'}
    )

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if email is not None and password:
            self.user_cache = authenticate(
                self.request, email=email, password=password
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data


class AccountCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput(attrs={'name': 'email'}),
        error_messages={'required': 'Email address is required.', 'invalid': 'Enter a valid email address.'}
    )
    first_name = forms.CharField(
        max_length=30,
        required=True,
        label='First Name',
        widget=forms.TextInput(attrs={'name': 'first_name'}),
        error_messages={'required': 'First name is required.'}
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        label='Last Name',
        widget=forms.TextInput(attrs={'name': 'last_name'}),
        error_messages={'required': 'Last name is required.'}
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user


class AccountPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        required=True,
        label=_('Email'),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'}),
        error_messages={'required': 'Email address is required.', 'invalid': 'Enter a valid email address.'}
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError(_('There is no user registered with the specified email address.'), code='invalid')
        return email
