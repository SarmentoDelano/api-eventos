# Generated by Django 5.1.3 on 2024-12-13 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventin', '0005_alter_participante_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participante',
            name='cpf',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='participante',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
