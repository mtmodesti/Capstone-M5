# Generated by Django 4.0.6 on 2022-07-13 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convenios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convenio',
            name='tipo',
            field=models.CharField(max_length=127, unique=True),
        ),
    ]
