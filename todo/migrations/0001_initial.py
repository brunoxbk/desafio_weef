# Generated by Django 4.2.3 on 2023-07-10 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(
                    max_length=150, verbose_name='Descrição')),
                ('checked', models.BooleanField(
                    default=False, verbose_name='Feito')),
                ('created', models.DateTimeField(
                    auto_now_add=True, verbose_name='Criado')),
                ('updated', models.DateTimeField(
                    auto_now=True, verbose_name='Alterado')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Itens',
                'ordering': ['-pk'],
            },
        ),
    ]