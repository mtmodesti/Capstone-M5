# Generated by Django 4.0.6 on 2022-07-12 13:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('nome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('telefone', models.CharField(max_length=30)),
                ('data_nascimento', models.DateTimeField()),
                ('data_cadastro', models.DateTimeField()),
            ],
        ),
    ]