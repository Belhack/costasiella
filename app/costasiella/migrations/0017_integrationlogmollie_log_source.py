# Generated by Django 2.2.10 on 2020-04-12 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costasiella', '0016_auto_20200412_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='integrationlogmollie',
            name='log_source',
            field=models.CharField(choices=[('ORDER_PAY', 'Order pay'), ('INVOICE_PAY', 'Invoice pay'), ('WEBHOOK', 'Webhook')], default='ORDER_PAY', max_length=255),
            preserve_default=False,
        ),
    ]