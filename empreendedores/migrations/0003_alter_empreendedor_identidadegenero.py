# Generated by Django 3.2.9 on 2025-02-25 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empreendedores', '0002_auto_20250218_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empreendedor',
            name='identidadegenero',
            field=models.CharField(choices=[('select_ident', 'Selecione a sua identidade de genero'), ('transmasculine', 'Transmasculine'), ('homem_trans', 'Homem Transgênero'), ('travesti', 'Travesti'), ('mulher_trans', 'Mulher Transgênero'), ('nao_binario', 'Não Binário'), ('outro', 'Outro'), ('prefiro_nao_dizer', 'Prefiro não dizer')], default='select_ident', max_length=20, verbose_name='Identidade de Gênero'),
        ),
    ]
