# Generated by Django 3.1.5 on 2021-05-18 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('costasiella', '0014_auto_20210518_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financepaymentbatch',
            name='organization_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='costasiella.organizationlocation'),
        ),
    ]