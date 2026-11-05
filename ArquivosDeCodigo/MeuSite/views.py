from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from datetime import date
from banco_de_dados.models import Usuario, Cuidado

def home(request):
    '''
    View function for home page of site.
    Renders the home.html template.
    '''
    return render(request, 'home.html')

def PerfilSaude(request):
    return render(request, 'PerfilSaude.html')

def ComoUsar(request):


    return render(request, 'ComoUsar.html')


def EsqueciSenha (request):


    return render(request, 'EsqueciSenha.html')

def ConsentimentoDados(request):
    return render(request, 'ConsentimentoDados.html')

def CriarConta (request):


    return render(request, 'CriarConta.html')

def Artigos (request):


    return render(request, 'Artigos.html')

def EdicaoUsuario(request):

    return render(request, 'EdicaoUsuario.html')

def PreferenciasNotificacoes(request):
    return render(request, 'PreferenciasNotificacoes.html')

def RemocaoUsuario(request):

    return render(request, 'RemocaoUsuario.html')

def Tela(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        usuario = Usuario.objects.filter(email=email).first()

        if usuario and check_password(senha, usuario.senha):
            return redirect('home')

        return render(request, 'Tela.html', {'erro': 'E-mail ou senha incorretos.'})

    return render(request, 'Tela.html')

def HistoricoFamiliar(request):

    return render(request, 'HistoricoFamiliar.html')

def CheckupInteligente(request):
    return render(request, 'CheckupInteligente.html')

def ListarUsuarios(request):

    usuarios = Usuario.objects.all()

    return render(request, 'ListarUsuarios.html', {'usuarios': usuarios})


def CalendarioCuidados(request):

    cuidados = Cuidado.objects.order_by('data')
    hoje = date.today()

    return render(request, 'CalendarioCuidados.html', {'cuidados': cuidados, 'hoje': hoje})

def RelatorioPreventivo(request):
    return render(request, 'RelatorioPreventivo.html')

def Familiares(request):

    return render(request, 'Familiares.html')
    