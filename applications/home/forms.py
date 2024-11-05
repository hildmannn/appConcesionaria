from django import forms
from .models import Usuarios
from django.contrib.auth import authenticate

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuarios
        fields = ['email', 'nombre', 'apellido', 'direccion', 'telefono', 'dni', 'role']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if Usuarios.objects.filter(email=email).exists():
            raise forms.ValidationError("El correo electrónico ya está en uso.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    email = forms.EmailField(label="Correo Electrónico")
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        if email and password:
            user = authenticate(username=email, password=password)
            if user is None:
                raise forms.ValidationError("Credenciales inválidas.")
        return cleaned_data
