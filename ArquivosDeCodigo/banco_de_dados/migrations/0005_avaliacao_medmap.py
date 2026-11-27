from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banco_de_dados', '0004_cuidado_detalhes'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvaliacaoMedMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False, verbose_name='ID')),
                ('nota', models.PositiveSmallIntegerField()),
                ('comentario', models.TextField(blank=True, default='')),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('usuario', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE, to='banco_de_dados.usuario'
                )),
            ],
        ),
    ]
