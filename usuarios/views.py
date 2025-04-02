from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import auth

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')  # Verifique o caminho do template

    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if senha != confirmar_senha:
            messages.error(request, 'Senha e confirmar senha devem ser iguais.')
            return redirect('cadastro/')
        
        if len(senha) < 6:
            messages.error(request, 'A senha deve ter mais de 6 caracteres.')
            return redirect('cadastro/') 

        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(request, 'Já existe um usuário com este nome.')
            return redirect('cadastro/')       

        User.objects.create_user(username=username, password=senha)
        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('login/')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html') 

    elif request.method == 'POST':
        username = request.POST.get('username') 
        senha = request.POST.get('senha')

        user = authenticate(request, username=username, password=senha)

        if user:
            auth_login(request, user)
            return redirect('/mentorados/') 

        messages.error(request, 'Nome ou senha inválidos.')
        return redirect('login/')
