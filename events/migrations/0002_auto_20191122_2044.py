# Generated by Django 2.2.6 on 2019-11-22 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Мероприятия', 'verbose_name_plural': 'Мероприятии'},
        ),
        migrations.AlterModelOptions(
            name='ticket',
            options={'verbose_name': 'Билет', 'verbose_name_plural': 'Билеты'},
        ),
    ]
