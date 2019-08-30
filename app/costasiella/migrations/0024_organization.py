# Generated by Django 2.2.2 on 2019-08-05 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costasiella', '0023_auto_20190802_1117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archived', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField(default='')),
                ('phone', models.CharField(max_length=255)),
                ('email', models.EmailField(default='', max_length=254)),
                ('registration', models.CharField(max_length=255)),
                ('tax_registration', models.CharField(max_length=255)),
            ],
        ),
    ]