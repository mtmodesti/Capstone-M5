# Generated by Django 4.0.6 on 2022-07-13 22:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anamneses', '0004_alter_anamnese_criado_em'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anamnese',
            name='criado_em',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 7, 13, 22, 43, 30, 116675)),
        ),
    ]
