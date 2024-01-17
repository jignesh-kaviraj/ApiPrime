from django.db import models
from datetime import datetime
# Create your models here.


class AppInfo(models.Model):
    device = models.CharField(max_length=200, null=True, blank=True)
    version = models.CharField(max_length=200, null=True, blank=True)
    url = models.CharField(max_length=200, null=True, blank=True)
    total_download = models.CharField(max_length=200, null=True, blank=True)
    force_update = models.BooleanField(default=False)
    is_video_download = models.BooleanField(default=False)

    def __str__(self):
        return self.device

class Report(models.Model):
    device_id = models.CharField(max_length=200, null=True, blank=True, unique=True)
    device_name = models.ForeignKey(AppInfo,on_delete=models.CASCADE, null=True, blank=True)
    first_login_date = models.DateTimeField(default=datetime.now(), null=True, blank=True)
    last_login_date = models.DateTimeField(default=datetime.now(), null=True, blank=True)
