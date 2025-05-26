from django.shortcuts import render , redirect
from django.contrib.auth import logout as django_logout
from django.contrib.auth import authenticate, login
from .forms import LoginForm , RegisterModelForm


def login_page(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return redirect('shop:index')
            else:
                return redirect('shop:index')
    return render(request, 'shop/login.html', {'form': form})


def logout(request):
    django_logout(request)
    return redirect('shop:index')

def register(request):
    form = RegisterModelForm()
    if request.method == 'POST':
        form = RegisterModelForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('users:login')
    return render(request, 'shop/register.html', {'form': form})
