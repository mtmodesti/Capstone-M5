# Generated by Django 4.0.6 on 2022-08-16 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0008_alter_paciente_convenio'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='status',
            field=models.CharField(default='Ok', max_length=50),
        ),
    ]
