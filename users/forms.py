from django import forms
from .models import CustomUser

from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            return username
        else:
            raise forms.ValidationError("User not found")

    def clean_password(self):
        password = self.data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters")
        return password


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username',)


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('username',)


from django import forms
from django.core.exceptions import ValidationError


class RegisterModelForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'confirm_password')
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise ValidationError("Parollar mos emas.")

        return cleaned_data


