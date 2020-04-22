from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreationForm
from django.views.decorators.http import require_POST

# Create your views here.
def signup(request):
    # 로그인시
    if request.user.is_authenticated:
        return redirect('community:index')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('community:index')
        else:
            return redirect('accounts:signup')
    
    # form => 유효하지 않을 때
    form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'sign_up.html', context)

def signin(request):
    # 로그인 되어있을 경우
    if request.user.is_authenticated:
        return redirect('community:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'community:index')
    # invalid
    form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'sign_in.html', context)

@login_required
def signout(request):
    auth_logout(request)
    return redirect('community:index')

