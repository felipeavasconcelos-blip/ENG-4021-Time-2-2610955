from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST

from banco_de_dados.models import Cuidado


@require_POST
def salvar_detalhes(request, cuidado_id):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('Tela')

    cuidado = get_object_or_404(
        Cuidado, pk=cuidado_id, perfil__usuario_id=usuario_id
    )
    local = request.POST.get('local', '').strip()
    observacoes = request.POST.get('observacoes', '').strip()
    if len(local) > 120 or len(observacoes) > 400:
        return redirect('CalendarioCuidados')

    cuidado.local = local
    cuidado.observacoes = observacoes
    cuidado.save(update_fields=['local', 'observacoes'])
    return redirect('CalendarioCuidados')
