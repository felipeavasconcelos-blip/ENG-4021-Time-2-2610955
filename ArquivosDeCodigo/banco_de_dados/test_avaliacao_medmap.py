from datetime import date

from django.test import TestCase
from django.urls import reverse

from banco_de_dados.models import AvaliacaoMedMap, Usuario


class TestesAvaliacaoMedMap(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create(nome='Pessoa', email='avaliar@teste.com', senha='teste')
        sessao = self.client.session
        sessao['usuario_id'] = self.usuario.pk
        sessao.save()

    def test_usuario_consegue_enviar_nota_e_comentario(self):
        resposta = self.client.post(reverse('AvaliacaoMedMap'), {
            'nota': '5', 'comentario': 'Gostei do calendário.'
        })
        self.assertEqual(resposta.status_code, 302)
        avaliacao = AvaliacaoMedMap.objects.get(usuario=self.usuario)
        self.assertEqual(avaliacao.nota, 5)
        self.assertEqual(avaliacao.comentario, 'Gostei do calendário.')

    def test_reenvio_atualiza_ao_inves_de_duplicar(self):
        url = reverse('AvaliacaoMedMap')
        self.client.post(url, {'nota': '4', 'comentario': 'Boa experiência'})
        self.client.post(url, {'nota': '5', 'comentario': 'Muito boa'})
        self.assertEqual(AvaliacaoMedMap.objects.filter(usuario=self.usuario).count(), 1)
        self.assertEqual(AvaliacaoMedMap.objects.get(usuario=self.usuario).nota, 5)

    def test_rejeita_nota_fora_da_faixa(self):
        resposta = self.client.post(reverse('AvaliacaoMedMap'), {
            'nota': '10', 'comentario': 'Teste'
        })
        self.assertContains(resposta, 'Escolha uma nota de 1 a 5.')
        self.assertFalse(AvaliacaoMedMap.objects.exists())

    def test_rejeita_comentario_acima_do_limite(self):
        self.client.post(reverse('AvaliacaoMedMap'), {
            'nota': '5', 'comentario': 'a' * 501
        })
        self.assertFalse(AvaliacaoMedMap.objects.exists())

    def test_necessita_login(self):
        self.client.session.flush()
        resposta = self.client.get(reverse('AvaliacaoMedMap'))
        self.assertEqual(resposta.status_code, 302)

    def test_nao_mostra_comentario_de_outra_pessoa(self):
        outra = Usuario.objects.create(nome='Outra', email='avaliar-outra@teste.com', senha='teste')
        AvaliacaoMedMap.objects.create(usuario=outra, nota=1, comentario='Comentário privado')
        resposta = self.client.get(reverse('AvaliacaoMedMap'))
        self.assertNotContains(resposta, 'Comentário privado')
