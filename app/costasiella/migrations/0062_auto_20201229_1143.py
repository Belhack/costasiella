# Generated by Django 3.0.8 on 2020-12-29 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('costasiella', '0061_auto_20201228_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduleeventticketscheduleitem',
            name='schedule_event_ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ticket_schedule_items', to='costasiella.ScheduleEventTicket'),
        ),
    ]