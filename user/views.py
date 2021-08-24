from django.shortcuts import render

from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserCreationForm


def registration(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Bienvenue {username}, votre compte a été créé avec succès. Vous pouvez vous connecter maintenant')
            return redirect('login')
    else:
        form = UserCreationForm()

    context ={'title':'registration', 'form':form}
    return render(request, 'register/registration.html', context)





def login_user(request):
    if request.method == 'POST':
        form = LoginForm()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        
        else:
            messages.warning(request, "Mot de passe ou Nom d'utilisateur incorrect")

    else:
        form = LoginForm()

    return render(request, 'register/login.html',{'title':"login", 'form':form})


def logout_user(request):
    logout(request)
    return render(request, 'lrn/index.html', {'title':'logout'})

    
