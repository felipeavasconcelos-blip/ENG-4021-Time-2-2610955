from django.contrib import admin
from .models import Usuario, Perfil, HistoricoFamiliar, Cuidado

admin.site.register(Usuario)
admin.site.register(Perfil)
admin.site.register(HistoricoFamiliar)
admin.site.register(Cuidado)