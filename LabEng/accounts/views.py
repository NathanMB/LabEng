from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import MedicoAuthenticationForm, MedicoChangeForm
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
                return render(request, 'login_user.html', args)

        else:
            return render(request, 'login_user.html', args)

    else:
        return redirect('home')

def exit_user(request):
    logout(request)
    return redirect('login_user')

def editar_perfil(request):
    if request.method == "POST":
        form = MedicoChangeForm(request.POST or None, request.FILES or None, instance=request.user)

        if form.is_valid():
            form.save()
            return render(request, 'editar_perfil.html', {'form': form})
        else:
            return render(request, 'editar_perfil.html', {'form': form})

    elif request.method == "GET":
        form = MedicoChangeForm(request.GET or None, request.FILES or None, instance=request.user)
        args = {'form': form}
        return render(request, 'editar_perfil.html', args)
