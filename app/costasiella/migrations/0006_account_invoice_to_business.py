# Generated by Django 4.0.6 on 2022-07-31 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('costasiella', '0005_auto_20220720_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='invoice_to_business',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='accounts', to='costasiella.business'),
        ),
    ]