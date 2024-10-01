from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="password")
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Confirm password")
    class Meta(UserCreationForm.Meta):
        fields=['username','email', 'first_name', 'last_name', 'password1', 'password2']
        widgets={
            'username':forms.TextInput(attrs={'class': 'form-control'}),
            'email':forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name':forms.TextInput(attrs={'class': 'form-control'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control'}),    
        }



class UserLoginForm(forms.Form):
        username=forms.CharField(max_length=60, widget=forms.TextInput(attrs={'class': "form-control"}))
        password=forms.CharField(max_length=68, widget=forms.PasswordInput(attrs={'class': "form-control"}))
     

