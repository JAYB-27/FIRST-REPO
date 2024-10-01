from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegistrationForm,UserLoginForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def signup(request):
    user_form=UserRegistrationForm()
    context= {
        "form" : user_form         
    }
    if request.method =="POST":
        form_with_data=UserRegistrationForm(request.POST)
        if form_with_data.is_valid():
             username=form_with_data.cleaned_data.get('username')
             user=User.objects.filter(username=username)
             if user.exists():
                 messages.error(request, "Username is already taken try a different one")
                 return redirect('user-signup')
             else:
                form_with_data.save()
                messages.success(request, "user created succefully")
                return redirect('home-page')
    return render(request, "accounts/signup.html", context)



def user_login(request):
    form = UserLoginForm()
    context = {
        "form": form
    }
    
    if request.method == "POST":
        form_data = UserLoginForm(request.POST)
        if form_data.is_valid():
            username = form_data.cleaned_data.get('username')
            password = form_data.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user=user)
                messages.success(request, "Login successful")
                return redirect('home-page')
            else:
                messages.error(request, "Invalid credentials")
    return render(request, "accounts/login.html", context)

        
        
        
        
        
        
