from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Enter Username'
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class':'form-control',
            'placeholder':'Enter Password',
            'id':'password'
        })
    )

    remember = forms.BooleanField(
        required=False
    )


 class RegisterForm(forms.ModelForm):

    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    email = forms.EmailField()

    username = forms.CharField(max_length=100)

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'id': 'password'})
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'id': 'confirm_password'})
    )

    class Meta:

        model = UserProfile

        fields = [

            'phone',
            'gender',
            'dob',
            'department',
            'skills',
            'address',
            'profile_picture'

        ]

    def clean(self):

        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm_password")

        if password != confirm:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data   