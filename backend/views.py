from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from rest_framework.views import APIView
from rest_framework.response import Response


class Register(APIView):
    def get(self, request):
        form = UserForm()

        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('index')

        return render(request, 'register.html', {'form': form})


class Login(APIView):
    def get(self, request):
        form = UserForm()

        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = UserForm()

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('index')

        return render(request, 'login.html', {'form': form, 'invalid': True})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

def index(request):
    return render(request, 'index.html', {})
