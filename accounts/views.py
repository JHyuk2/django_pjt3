from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from djangn.contrib.auth import login as auth_login
from djangn.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.decorators.http import required_POST

from .forms import CustomUserChangeForm

# Create your views here.
def signup(request):
    # 로그인시
    if request.user.is_authenticated:
        return redirect('community:index')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('community:index')
    
    # form => 유효하지 않을 때
    form = UserCreationForm()
    context = {
        'form':form,
    }
    return render(request, 'community/sign_up.html', context)

def signin(request):
    # 로그인 되어있을 경우
    if request.user.is_authenticated:
        return redirect('community:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_uesr())
            return redirect(request.GET.get('next') or 'community:index')
    # invalid
    form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request, 'community/sign_in.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('community:index')

