# Generated by Django 2.2.2 on 2019-08-02 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('costasiella', '0020_auto_20190802_0903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='financeinvoiceitem',
            old_name='subtotal',
            new_name='sub_total',
        ),
    ]