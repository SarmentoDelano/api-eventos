# Generated by Django 5.1.3 on 2024-12-12 00:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventin', '0003_alter_evento_capacidade_alter_evento_descricao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participante',
            name='cpf',
            field=models.CharField(max_length=11, unique=True, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]
