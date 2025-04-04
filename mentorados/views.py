from django.shortcuts import render, redirect
from django.http import HttpResponse
from. models import Mentorados, Navigators

def mentorados(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'GET':
        navigators = Navigators.objects.filter(user=request.user)
        return render (request, 'mentorados.html', {'estagios': Mentorados.estagio_choices, 'navigators': navigators})
