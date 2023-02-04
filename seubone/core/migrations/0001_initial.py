# Generated by Django 4.1.6 on 2023-02-04 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tecido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('LINHO', 'Linho'), ('CAMURÇA', 'Camurça'), ('MESCLA', 'Mescla'), ('MOLETOM', 'Moletom')], max_length=50)),
                ('cor', models.CharField(choices=[('AZUL', 'Azul'), ('AMARELO', 'Amarelo'), ('VERMELHO', 'Vermelho'), ('VERDE', 'Verde')], max_length=50)),
                ('metros', models.IntegerField()),
            ],
        ),
    ]
