
from django.contrib import admin
from django.urls import path
from .views import Download, AppInfoView

urlpatterns = [
    path('download/', Download.as_view(), name='download'),
    path('app_info/', AppInfoView.as_view(), name="app_info"),
]
