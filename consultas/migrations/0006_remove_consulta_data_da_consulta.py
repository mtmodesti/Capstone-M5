# Generated by Django 4.0.6 on 2022-07-14 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0005_alter_consulta_criado_em'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consulta',
            name='data_da_consulta',
        ),
    ]
