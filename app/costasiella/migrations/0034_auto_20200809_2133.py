# Generated by Django 3.0.8 on 2020-08-09 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('costasiella', '0033_auto_20200805_1334'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'permissions': [('view_automation', 'Can view automation menu'), ('view_insight', 'Can view insight menu'), ('view_insightclasspassesactive', 'Can view insight classpasses active'), ('view_insightclasspassessold', 'Can view insight classpasses sold'), ('view_insightsubscriptionsactive', 'Can view insight subscriptions active'), ('view_insightsubscriptionssold', 'Can view insight subscriptions sold'), ('view_selfcheckin', 'Can use the selfcheckin feature')]},
        ),
    ]
