# Generated by Django 5.0.6 on 2024-08-16 20:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_clientcompanycalendar_clientcompanyevent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientcompanyevent',
            name='calendar',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='companyEvents',
                to='client.clientcompanycalendar',
            ),
        ),
    ]
