# Generated by Django 4.2.1 on 2023-08-31 18:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApplikacijaZaSportskaOpremaApp', '0013_remove_orderitem_user_alter_order_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2023, 8, 31, 20, 56, 56, 38744)),
        ),
    ]
