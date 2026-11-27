from django.shortcuts import get_object_or_404, redirect, render

from banco_de_dados.models import AvaliacaoMedMap, Usuario


def avaliar_medmap(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('Tela')

    usuario = get_object_or_404(Usuario, pk=usuario_id)
    avaliacao = AvaliacaoMedMap.objects.filter(usuario=usuario).first()
    erro = ''

    if request.method == 'POST':
        nota_texto = request.POST.get('nota', '').strip()
        comentario = request.POST.get('comentario', '').strip()
        if nota_texto not in ('1', '2', '3', '4', '5'):
            erro = 'Escolha uma nota de 1 a 5.'
        elif len(comentario) > 500:
            erro = 'O comentário deve ter até 500 caracteres.'
        else:
            AvaliacaoMedMap.objects.update_or_create(
                usuario=usuario,
                defaults={'nota': int(nota_texto), 'comentario': comentario},
            )
            return redirect('AvaliacaoMedMap')

    return render(request, 'AvaliacaoMedMap.html', {
        'avaliacao': avaliacao,
        'erro': erro,
        'enviado': bool(avaliacao),
        'usuario': usuario,
    })
