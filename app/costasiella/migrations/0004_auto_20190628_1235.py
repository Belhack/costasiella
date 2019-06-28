# Generated by Django 2.2.2 on 2019-06-28 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costasiella', '0003_remove_account_search_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='customer',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='account',
            name='employee',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='teacher',
            field=models.BooleanField(default=False),
        ),
    ]
