# Generated by Django 3.1.5 on 2021-05-20 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costasiella', '0016_accountbankaccount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountbankaccount',
            name='bic',
            field=models.CharField(default='', max_length=255),
        ),
    ]