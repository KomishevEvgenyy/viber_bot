# Generated by Django 2.2.6 on 2019-11-22 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobposition',
            options={'verbose_name': 'Должность', 'verbose_name_plural': 'Должностя'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
