from django.contrib import admin
from .models import AppInfo, Report

@admin.register(AppInfo)
class AppInfoAdmin(admin.ModelAdmin):
    list_display = ("device", "version", "url", "total_download", "force_update","is_video_download")


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ("device_id","device_name","first_login_date", "last_login_date",)
