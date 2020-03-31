from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import MedicoAuthenticationForm
# Create your views here.

def login_user(request):
    if request.user.is_authenticated == False:
        form = MedicoAuthenticationForm(request.POST or None)
        args = {'form': form }

        if request.POST:
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, username=email, password=password)

            if form.is_valid and user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Email ou senha incorreto')
                return render(request, 'login_user.html')

        else:
            return render(request, 'login_user.html', args)

    else:
        return redirect('home')

def exit_user(request):
    logout(request)
    return redirect('login_user')
