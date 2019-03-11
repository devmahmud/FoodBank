from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your username'}),
                               help_text="<small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small>")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Enter your Email Address'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your Last Name'}))
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}),
                                    help_text="<small><ul><li>Your password can't be too similar to your other personal information.</li>\
                                    <li>Your password must contain at least 8 characters.</li>\
                                    <li>Your password can't be a commonly used password.</li>\
                                    <li>Your password can't be entirely numeric.</li></ul></small>")
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput(attrs={'class': 'form-control'}),\
                                help_text="<small>Enter the same password as before, for verification.</small>")
    class Meta:
        model = User
        fields=['username','email','first_name','last_name','password1', 'password2',]
