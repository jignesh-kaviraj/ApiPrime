# Generated by Django 5.0 on 2024-01-02 17:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apis', '0002_appinfo_is_download_alter_report_first_login_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appinfo',
            old_name='is_download',
            new_name='can_video_download',
        ),
        migrations.AlterField(
            model_name='report',
            name='first_login_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 2, 23, 17, 8, 441274), null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='last_login_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 2, 23, 17, 8, 441274), null=True),
        ),
    ]
