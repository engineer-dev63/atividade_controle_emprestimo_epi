from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Colaborador
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



# funcao de cadstrar usuarios------------------------------

def cadastrar_usuario(request):
    if request.method == 'POST':
        # 1. Captura os dados do HTML
        nome = request.POST.get('nome')
        cargo = request.POST.get('cargo')
        matricula = request.POST.get('matricula')

        # 2. Validação simples: checa se o usuário já existe no Banco de Dados
        # if User.objects.filter(matricula=nome).exists():
        #     messages.error(request, "Esta matricula já pretence a outro colaborador.")
        #     return render(request, 'colaboradores.html')
        
        # 3. Cria e salva o usuário no banco com a matricula criptografada
        User.objects.create_user(nome=nome, cargo=cargo, matricula=matricula)
        
        # 4. Redireciona para a tela de login após o sucesso
        messages.success(request, "Usuário cadastrado com sucesso!")
        # return redirect('') # Nome da rota da sua view de login
        
    return render(request, 'colaboradores.html')