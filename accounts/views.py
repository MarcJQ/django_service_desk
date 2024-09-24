from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone

from django.contrib.auth import login
from .models import CustomUser, UserProfile
from . import forms

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = CustomUser.objects.get(username=username)
            if user.check_password(password):
                login(request, user)
                return redirect('home')
    else:
        form = forms.LoginForm()
    return render(request, 'login.html', {'form': form})

class LoginView(auth_views.LoginView):
    """
    Display the login form and handle the login action.
    """
    template_name = 'login.html'



