from django.contrib.auth.backends import ModelBackend
from .models import Usuarios

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Usuarios.objects.get(email=username)
        except Usuarios.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None
