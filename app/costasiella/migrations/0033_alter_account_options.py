# Generated by Django 4.1.7 on 2023-03-01 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('costasiella', '0032_scheduleitem_count_enrolled_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'permissions': [('view_automation', 'Can view automation menu'), ('view_insight', 'Can view insight menu'), ('view_insightaccountsinactive', 'Can view insight accounts inactive'), ('view_insightclasspasses', 'Can view insight classpasses active'), ('view_insightfinancetaxratesummary', 'Can view insight finance tax rates summary'), ('view_insightinstructorclassesmonth', 'Can view insight instructor classes in month'), ('view_insightrevenue', 'Can view insight subscriptions sold'), ('view_insightsubscriptions', 'Can view insight subscriptions'), ('view_insighttrialpasses', 'Can view insight trial passes'), ('view_selfcheckin', 'Can use the selfcheckin feature')]},
        ),
    ]