from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def  home(request):
    return render(request, 'app_epicontrol/base.html')

def colaboradores(request):
    return render(request, 'app_epicontrol/colaboradores.html')

def emprestimos(request):
    return render(request, 'app_epicontrol/emprestimos.html')

def equipamentos(request):
    return render(request, 'app_epicontrol/equipamentos.html')