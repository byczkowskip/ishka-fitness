from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.base_user import AbstractBaseUser


class AuthEmailBackend(BaseBackend):
    def authenticate(self, request, email: str|None = None, password: str|None = None, **kwargs) -> AbstractBaseUser|None:
        user = get_user_model()
        try:
            user = user.objects.get(email=email)
        except user.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id) -> AbstractBaseUser|None:
        user = get_user_model()
        try:
            return user.objects.get(pk=user_id)
        except user.DoesNotExist:
            return None
