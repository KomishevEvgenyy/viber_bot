# Generated by Django 2.2.6 on 2019-11-12 18:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vbot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viberuser',
            name='country',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='viberuser',
            name='language',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='viberuser',
            name='name',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='viberuser',
            name='phone_number',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='viberuser',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
