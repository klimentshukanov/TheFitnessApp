# Generated by Django 4.2.1 on 2023-08-30 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ApplikacijaZaSportskaOpremaApp', '0004_produkt_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='produkt',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
