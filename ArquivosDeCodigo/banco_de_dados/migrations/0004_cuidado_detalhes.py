from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banco_de_dados', '0003_perfil_habitos'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuidado',
            name='local',
            field=models.CharField(blank=True, default='', max_length=120),
        ),
        migrations.AddField(
            model_name='cuidado',
            name='observacoes',
            field=models.TextField(blank=True, default=''),
        ),
    ]
