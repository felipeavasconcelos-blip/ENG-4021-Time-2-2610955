from datetime import timedelta

from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils import timezone

from banco_de_dados.models import Cuidado


def escapar_ics(texto):
    """Protege caracteres especiais usados no formato iCalendar."""
    return (
        str(texto).replace('\\', '\\\\')
        .replace('\r\n', '\n').replace('\r', '\n')
        .replace('\n', '\\n').replace(';', '\\;').replace(',', '\\,')
    )


def dobrar_linha(linha):
    """Quebra linhas grandes em até 75 bytes, continuando com espaço."""
    resultado = []
    atual = ''
    limite = 75
    for caractere in linha:
        tamanho = len((atual + caractere).encode('utf-8'))
        if atual and tamanho > limite:
            resultado.append(atual)
            atual = ' ' + caractere
            limite = 75
        else:
            atual += caractere
    resultado.append(atual)
    return '\r\n'.join(resultado)


def exportar_cuidados(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('Tela')

    hoje = timezone.localdate()
    cuidados = Cuidado.objects.filter(
        perfil__usuario_id=usuario_id,
        concluido=False,
        data__gte=hoje
    ).order_by('data', 'id')

    linhas = [
        'BEGIN:VCALENDAR',
        'VERSION:2.0',
        'PRODID:-//MedMap//Calendario de Cuidados//PT-BR',
        'CALSCALE:GREGORIAN',
        'METHOD:PUBLISH',
    ]
    agora = timezone.now().strftime('%Y%m%dT%H%M%SZ')

    for cuidado in cuidados:
        inicio = cuidado.data.strftime('%Y%m%d')
        fim = (cuidado.data + timedelta(days=1)).strftime('%Y%m%d')
        linhas.extend([
            'BEGIN:VEVENT',
            f'UID:medmap-{usuario_id}-{cuidado.pk}@medmap.local',
            f'DTSTAMP:{agora}',
            f'DTSTART;VALUE=DATE:{inicio}',
            f'DTEND;VALUE=DATE:{fim}',
            f'SUMMARY:{escapar_ics(cuidado.nome)}',
            f'DESCRIPTION:{escapar_ics("Tipo: " + cuidado.tipo)}',
            'END:VEVENT',
        ])

    linhas.append('END:VCALENDAR')
    conteudo = '\r\n'.join(dobrar_linha(l) for l in linhas) + '\r\n'
    resposta = HttpResponse(conteudo, content_type='text/calendar; charset=utf-8')
    resposta['Content-Disposition'] = 'attachment; filename="medmap-cuidados.ics"'
    resposta['Cache-Control'] = 'private, no-store'
    return resposta
