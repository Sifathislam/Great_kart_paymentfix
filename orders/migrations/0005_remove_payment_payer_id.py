# Generated by Django 5.0.3 on 2024-06-23 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_payment_payer_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='payer_id',
        ),
    ]
