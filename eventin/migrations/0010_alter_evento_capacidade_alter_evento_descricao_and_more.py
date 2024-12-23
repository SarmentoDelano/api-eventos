# Generated by Django 5.1.4 on 2024-12-13 01:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventin', '0009_alter_participante_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='capacidade',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinLengthValidator(1)]),
        ),
        migrations.AlterField(
            model_name='evento',
            name='descricao',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(10)]),
        ),
        migrations.AlterField(
            model_name='evento',
            name='local',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
        migrations.AlterField(
            model_name='evento',
            name='titulo',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
        migrations.AlterField(
            model_name='participante',
            name='nome',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]
