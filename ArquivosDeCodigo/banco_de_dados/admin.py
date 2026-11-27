from django.contrib import admin
from .models import Usuario, Perfil, HistoricoFamiliar, Cuidado, AvaliacaoMedMap

admin.site.register(Usuario)
admin.site.register(Perfil)
admin.site.register(HistoricoFamiliar)
admin.site.register(Cuidado)


@admin.register(AvaliacaoMedMap)
class AvaliacaoMedMapAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'nota', 'atualizado_em')
    search_fields = ('usuario__nome', 'usuario__email')
    readonly_fields = ('usuario', 'nota', 'comentario', 'atualizado_em')
