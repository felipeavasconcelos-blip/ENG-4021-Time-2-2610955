from datetime import date

from django.test import TestCase
from django.urls import reverse

from banco_de_dados.models import Cuidado, Perfil, Usuario


class TestesDetalhesCuidados(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create(
            nome='Teste', email='detalhes@teste.com', senha='teste'
        )
        self.perfil = Perfil.objects.create(
            usuario=self.usuario, nome='Teste', sexo='Outro',
            data_nascimento=date(2000, 1, 1)
        )
        sessao = self.client.session
        sessao['usuario_id'] = self.usuario.pk
        sessao.save()

    def test_cadastro_salva_local_e_observacoes(self):
        self.client.post(reverse('CadastroCuidados'), {
            'tipo': 'Consulta',
            'nome': 'Consulta clínica',
            'data': '2026-12-10',
            'local': 'Clínica Central',
            'observacoes': 'Levar exames'
        })
        cuidado = Cuidado.objects.get(perfil=self.perfil)
        self.assertEqual(cuidado.local, 'Clínica Central')
        self.assertEqual(cuidado.observacoes, 'Levar exames')

    def test_campos_opcionais_aceitam_vazio(self):
        self.client.post(reverse('CadastroCuidados'), {
            'tipo': 'Exame', 'nome': 'Hemograma', 'data': '2026-12-11'
        })
        cuidado = Cuidado.objects.get(perfil=self.perfil)
        self.assertEqual(cuidado.local, '')
        self.assertEqual(cuidado.observacoes, '')

    def test_edita_e_exibe_detalhes_no_calendario(self):
        cuidado = Cuidado.objects.create(perfil=self.perfil, nome='Vacina',
                                         tipo='Vacina', data=date(2026, 12, 12))
        self.client.post(reverse('DetalhesCuidado', args=[cuidado.pk]), {
            'local': 'Posto Central', 'observacoes': 'Levar documento'
        })
        cuidado.refresh_from_db()
        self.assertEqual(cuidado.local, 'Posto Central')
        self.assertContains(self.client.get(reverse('CalendarioCuidados')), 'Levar documento')

    def test_nao_edita_cuidado_de_outra_conta(self):
        outro = Usuario.objects.create(nome='Outro', email='outro-detalhes@teste.com',
                                       senha='teste')
        perfil = Perfil.objects.create(usuario=outro, nome='Outro',
                                      data_nascimento=date(1990, 1, 1), sexo='Outro')
        cuidado = Cuidado.objects.create(perfil=perfil, tipo='Exame',
                                         nome='Exame de outra pessoa', data=date(2026, 12, 12))
        resposta = self.client.post(reverse('DetalhesCuidado', args=[cuidado.pk]),
                                    {'local': 'Indevido', 'observacoes': ''})
        self.assertEqual(resposta.status_code, 404)
        cuidado.refresh_from_db()
        self.assertEqual(cuidado.local, '')

    def test_nao_aceita_detalhes_excessivamente_longos(self):
        cuidado = Cuidado.objects.create(perfil=self.perfil, tipo='Exame',
                                         nome='Exame', data=date(2026, 12, 12))
        self.client.post(reverse('DetalhesCuidado', args=[cuidado.pk]), {
            'local': 'a' * 121, 'observacoes': ''
        })
        cuidado.refresh_from_db()
        self.assertEqual(cuidado.local, '')
