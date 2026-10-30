from django.shortcuts import render

def home(request):
    '''
    View function for home page of site.
    Renders the home.html template.
    '''
    return render(request, 'home.html')

def ComoUsar(request):


    return render(request, 'ComoUsar.html')


def EsqueciSenha (request):


    return render(request, 'EsqueciSenha.html')

def CriarConta (request):


    return render(request, 'CriarConta.html')

def Artigos (request):


    return render(request, 'Artigos.html')

def EdicaoUsuario(request):

    return render(request, 'EdicaoUsuario.html')

def RemocaoUsuario(request):

    return render(request, 'RemocaoUsuario.html')

def Tela(request):


    return render(request, 'Tela.html')

def HistoricoFamiliar(request):

    return render(request, 'HistoricoFamiliar.html')

def ListarUsuarios(request):

    return render(request, 'ListarUsuarios.html')


def CalendarioCuidados(request):

    return render(request, 'CalendarioCuidados.html')
