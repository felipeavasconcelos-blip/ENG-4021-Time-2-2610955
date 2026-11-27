"""
URL configuration for MeuSite project.

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import path
from MeuSite import views
from MeuSite import cuidados_actions
from MeuSite import cuidados_detalhes
from MeuSite import exportar_calendario
from MeuSite import avaliacao

urlpatterns = [
    path('Cuidados/<int:cuidado_id>/atualizar/', cuidados_actions.atualizar_cuidado, name='AtualizarCuidado'),
    path('Cuidados/<int:cuidado_id>/detalhes/', cuidados_detalhes.salvar_detalhes, name='DetalhesCuidado'),
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('Artigos/', views.Artigos, name='Artigos'),
    path('ComoUsar/', views.ComoUsar, name='ComoUsar'),
    path('ConsentimentoDados/', views.ConsentimentoDados, name='ConsentimentoDados'),
    path('CriarConta/', views.CriarConta, name='CriarConta'),
    path('EdicaoUsuario/<int:usuario_id>/', views.EdicaoUsuario, name='EdicaoUsuario'),
    path('EsqueciSenha/', views.EsqueciSenha, name='EsqueciSenha'),
    path('PreferenciasNotificacoes/', views.PreferenciasNotificacoes, name='PreferenciasNotificacoes'),
    path('RemocaoUsuario/<int:usuario_id>/', views.RemocaoUsuario, name='RemocaoUsuario'),
    path('login/', views.Tela, name='Login'),
    path('Tela/', views.Tela, name='Tela'),
    path('HistoricoFamiliar/', views.HistoricoFamiliar, name='HistoricoFamiliar'),
    path('CheckupInteligente/', views.CheckupInteligente, name='CheckupInteligente'),
    path('ListarUsuarios/', views.ListarUsuarios, name='ListarUsuarios'),
    path('CalendarioCuidados/', views.CalendarioCuidados, name='CalendarioCuidados'),
    path('CalendarioCuidados/exportar/', exportar_calendario.exportar_cuidados, name='ExportarCalendario'),
    path('RelatorioPreventivo/', views.RelatorioPreventivo, name='RelatorioPreventivo'),
    path('Familiares/', views.Familiares, name='Familiares'),
    path('PerfilSaude/', views.PerfilSaude, name='PerfilSaude'),
    path('CadastroCuidados/', views.CadastroCuidados, name='CadastroCuidados'),
    path('InicioLogado/', views.InicioLogado, name='InicioLogado'),
    path('MinhaConta/', views.MinhaConta, name='MinhaConta'),
    path('TrocarConta/', views.TrocarConta, name='TrocarConta'),
    path('Sair/', views.Sair, name='Sair'),
    path('Avaliacao/', avaliacao.avaliar_medmap, name='AvaliacaoMedMap'),
]
