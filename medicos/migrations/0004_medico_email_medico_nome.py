# Generated by Django 4.0.6 on 2022-07-18 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicos', '0003_remove_medico_agenda'),
    ]

    operations = [
        migrations.AddField(
            model_name='medico',
            name='email',
            field=models.CharField(max_length=127, null=True),
        ),
        migrations.AddField(
            model_name='medico',
            name='nome',
            field=models.CharField(max_length=127, null=True),
        ),
    ]
