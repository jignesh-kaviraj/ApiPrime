# Generated by Django 5.0 on 2024-09-18 06:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apis', '0005_alter_report_device_id_alter_report_first_login_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='first_login_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 9, 18, 6, 13, 58, 675618), null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='last_login_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 9, 18, 6, 13, 58, 675641), null=True),
        ),
    ]
