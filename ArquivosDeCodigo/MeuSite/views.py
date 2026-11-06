from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from datetime import date
from django.utils.dateparse import parse_date
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
            return redirect('InicioLogado')

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
    # Filtros combinados aplicados no banco de dados.
    cuidados = Cuidado.objects.all()
    tipos_validos = ('Consulta', 'Exame', 'Vacina')

    tipo = request.GET.get('tipo', '')
    if tipo not in tipos_validos:
        tipo = ''
    if tipo:
        cuidados = cuidados.filter(tipo=tipo)

    inicio = request.GET.get('inicio', '')
    fim = request.GET.get('fim', '')
    mensagem_erro = ''

    try:
        inicio_data = parse_date(inicio) if inicio else None
    except ValueError:
        inicio_data = None

    try:
        fim_data = parse_date(fim) if fim else None
    except ValueError:
        fim_data = None

    if inicio and inicio_data is None:
        mensagem_erro = 'A data inicial informada é inválida.'
        inicio = ''
    if fim and fim_data is None:
        mensagem_erro = 'A data final informada é inválida.'
        fim = ''

    if inicio_data and fim_data and inicio_data > fim_data:
        mensagem_erro = 'A data inicial deve ser anterior ou igual à data final.'
        cuidados = Cuidado.objects.none()
    else:
        if inicio_data:
            cuidados = cuidados.filter(data__gte=inicio_data)
        if fim_data:
            cuidados = cuidados.filter(data__lte=fim_data)

    ordem = request.GET.get('ordem', 'asc')
    if ordem not in ('asc', 'desc'):
        ordem = 'asc'
    cuidados = cuidados.order_by('-data' if ordem == 'desc' else 'data', 'id')

    contexto = {
        'cuidados': cuidados,
        'hoje': date.today(),
        'tipos_cuidado': tipos_validos,
        'tipo_selecionado': tipo,
        'inicio': inicio,
        'fim': fim,
        'ordem': ordem,
        'mensagem_erro': mensagem_erro,
        'total_cuidados': cuidados.count(),
    }
    return render(request, 'CalendarioCuidados.html', contexto)

def RelatorioPreventivo(request):
    return render(request, 'RelatorioPreventivo.html')

def Familiares(request):

    return render(request, 'Familiares.html')

# View da tela de cadastro (formulário ainda sem gravação no banco).
def CadastroCuidados(request):
    return render(request, 'CadastroCuidados.html')

def InicioLogado(request):
    return render (request, 'InicioLogado.html')