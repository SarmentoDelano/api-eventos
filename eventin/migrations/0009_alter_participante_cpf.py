# Generated by Django 5.1.4 on 2024-12-13 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventin', '0008_alter_evento_descricao_alter_evento_local_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participante',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
