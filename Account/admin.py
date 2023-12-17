from django.contrib import admin
from Account.models import ErrorBase

# Register your models here.
@admin.register(ErrorBase)
class ErrorBaseAdmin(admin.ModelAdmin):
    list_display = ("class_name","level","message","traceback","created_on")