from datetime import date, timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from banco_de_dados.models import Cuidado, Perfil, Usuario


class TestesExportacaoICS(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create(nome='Pessoa', email='ics@teste.com', senha='teste')
        self.perfil = Perfil.objects.create(
            usuario=self.usuario, nome='Pessoa', sexo='Outro',
            data_nascimento=date(2000, 1, 1)
        )
        sessao = self.client.session
        sessao['usuario_id'] = self.usuario.id
        sessao.save()

    def criar_cuidado(self, nome, dias, concluido=False, perfil=None):
        return Cuidado.objects.create(
            perfil=perfil or self.perfil, nome=nome, tipo='Consulta',
            data=timezone.localdate() + timedelta(days=dias),
            concluido=concluido
        )

    def test_download_inclui_apenas_pendentes_futuros(self):
        self.criar_cuidado('Consulta importante', 3)
        self.criar_cuidado('Exame realizado', -1, True)
        self.criar_cuidado('Consulta passada', -3)
        resposta = self.client.get(reverse('ExportarCalendario'))
        texto = resposta.content.decode('utf-8')
        self.assertEqual(resposta.status_code, 200)
        self.assertTrue(resposta['Content-Type'].startswith('text/calendar'))
        self.assertIn('attachment;', resposta['Content-Disposition'])
        self.assertIn('BEGIN:VCALENDAR', texto)
        self.assertEqual(texto.count('BEGIN:VEVENT'), 1)
        self.assertIn('Consulta importante', texto)
        self.assertNotIn('Exame realizado', texto)
        self.assertNotIn('Consulta passada', texto)

    def test_nao_exporta_agenda_de_outras_contas(self):
        outro = Usuario.objects.create(nome='Outro', email='ics-outro@teste.com', senha='teste')
        perfil_outro = Perfil.objects.create(
            usuario=outro, nome='Outro', sexo='Outro',
            data_nascimento=date(2000, 1, 1)
        )
        self.criar_cuidado('Privado', 2, perfil=perfil_outro)
        resposta = self.client.get(reverse('ExportarCalendario'))
        self.assertNotIn('Privado', resposta.content.decode('utf-8'))

    def test_gera_calendario_vazio_valido(self):
        resposta = self.client.get(reverse('ExportarCalendario'))
        self.assertIn('END:VCALENDAR', resposta.content.decode('utf-8'))
        self.assertNotIn('BEGIN:VEVENT', resposta.content.decode('utf-8'))

    def test_necessita_sessao(self):
        self.client.session.flush()
        resposta = self.client.get(reverse('ExportarCalendario'))
        self.assertEqual(resposta.status_code, 302)

    def test_escapa_caracteres_especiais(self):
        from MeuSite.exportar_calendario import escapar_ics
        self.assertEqual(escapar_ics('A,B;C'), r'A\,B\;C')
