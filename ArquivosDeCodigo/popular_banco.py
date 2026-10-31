import os
import django
import random

from datetime import date, timedelta
from django.contrib.auth.hashers import make_password
from django.db import transaction



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MeuSite.settings')
django.setup()


from banco_de_dados.models import (
    Usuario,
    Perfil,
    HistoricoFamiliar,
    Cuidado
)



pessoas = [
    ("Ana Silva", "ana"),
    ("Bruno Costa", "bruno"),
    ("Carla Oliveira", "carla"),
    ("Daniel Santos", "daniel"),
    ("Eduarda Lima", "eduarda"),
    ("Fernando Souza", "fernando"),
    ("Gabriela Rocha", "gabriela"),
    ("Henrique Alves", "henrique"),
    ("Isabela Martins", "isabela"),
    ("João Pereira", "joao"),
]

parentes = [
    ("Mãe", "Diabetes tipo 2", 52),
    ("Pai", "Hipertensão", 48),
    ("Avó materna", "Doença cardiovascular", 67),
    ("Avô paterno", "Diabetes tipo 2", 70),
    ("Irmão", "Asma", 15),
    ("Tia", "Hipotireoidismo", 43),
    ("Avô materno", "Hipertensão", 61),
    ("Avó paterna", "Osteoporose", 72),
]

cuidados = [
    ("Consulta", "Consulta clínica"),
    ("Exame", "Hemograma completo"),
    ("Vacina", "Vacina contra gripe"),
    ("Exame", "Exame de glicemia"),
    ("Consulta", "Consulta cardiológica"),
    ("Exame", "Exame de colesterol"),
    ("Consulta", "Consulta nutricional"),
    ("Vacina", "Vacina contra tétano"),
]


def gerar_data_nascimento():
    inicio = date(1960, 1, 1)
    fim = date(2005, 12, 31)

    intervalo = (fim - inicio).days
    return inicio + timedelta(days=random.randint(0, intervalo))


@transaction.atomic
def popular_banco():

    random.seed(42)

    total_usuarios = 0
    total_perfis = 0
    total_historicos = 0
    total_cuidados = 0

    for i, (nome, identificador) in enumerate(pessoas, start=1):

        
        email = f"{identificador}@medmap.com"

        usuario, usuario_criado = Usuario.objects.get_or_create(
            email=email,
            defaults={
                "nome": nome,
                "senha": make_password("MedMapDemo123!")
            }
        )

        if usuario_criado:
            total_usuarios += 1

        
        perfil, perfil_criado = Perfil.objects.get_or_create(
            usuario=usuario,
            defaults={
                "nome": nome,
                "data_nascimento": gerar_data_nascimento(),
                "sexo": random.choice(["Masculino", "Feminino"])
            }
        )

        if perfil_criado:
            total_perfis += 1

        
        historicos_escolhidos = random.sample(parentes, 2)

        for parente, doenca, idade in historicos_escolhidos:

            _, criado = HistoricoFamiliar.objects.get_or_create(
                perfil=perfil,
                parente=parente,
                doenca=doenca,
                defaults={
                    "idade_diagnostico": idade
                }
            )

            if criado:
                total_historicos += 1

        
        cuidados_escolhidos = random.sample(cuidados, 3)

        for j, (tipo, nome_cuidado) in enumerate(cuidados_escolhidos):

            data_cuidado = date.today() + timedelta(
                days=(i * 10) + (j * 20)
            )

            _, criado = Cuidado.objects.get_or_create(
                perfil=perfil,
                tipo=tipo,
                nome=nome_cuidado,
                defaults={
                    "data": data_cuidado
                }
            )

            if criado:
                total_cuidados += 1

    print("\n===== POPULAÇÃO DO MEDMAP CONCLUÍDA =====")
    print(f"Novos usuários: {total_usuarios}")
    print(f"Novos perfis: {total_perfis}")
    print(f"Novos históricos familiares: {total_historicos}")
    print(f"Novos cuidados: {total_cuidados}")

    print("\nDados de acesso para demonstração:")
    print("Senha padrão: MedMapDemo123!")
    print("Exemplo de usuário: ana@medmap.com")

if __name__ == "__main__":
    popular_banco()
