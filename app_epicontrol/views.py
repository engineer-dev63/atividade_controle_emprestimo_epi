from django.shortcuts import render, redirect
from django.contrib import messages
from .bd_improvisado import inserir_colaborador, listar_colaboradores,pesquisar_colaborador, editar_colaborador, deletar_colaborador

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





def colaboradores(request):
    lista = listar_colaboradores()

    # PESQUISA
    if request.method == "GET":
        busca = request.GET.get("busca")
        if busca:
            lista = pesquisar_colaborador(busca)

    return render(request, 'app_epicontrol/colaboradores.html', {
        "colaboradores": lista
    })


# CREATE
def cadastrar_usuario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cargo = request.POST.get('cargo')
        matricula = request.POST.get('matricula')

        inserir_colaborador(nome, cargo, matricula)

    return redirect('colaboradores')




# UPDATE
def editar_usuario(request, id):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cargo = request.POST.get('cargo')
        matricula = request.POST.get('matricula')

        editar_colaborador(id, nome, cargo, matricula)

    return redirect('colaboradores')



def excluir_colaborador(request, id):
    if request.method == "POST":
        deletar_colaborador(id)

    return redirect("colaboradores")