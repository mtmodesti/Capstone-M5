# Generated by Django 4.0.6 on 2022-07-13 13:59

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
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 13, 10, 59, 20, 128315)),
        ),
    ]
