
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', DownloadPageMW.as_view(), name='download_page_mw'),
    path('download/', Download.as_view(), name='download'),
    path('app_info/', AppInfoView.as_view(), name="app_info"),
    path('download_mw/', DownloadMW.as_view(), name="download_mw"),
]
