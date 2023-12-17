from django.db import models
import logging

from django.utils.translation import gettext_lazy as _

# Create your models here.
LOG_LEVELS = (
    (logging.INFO, _("info")),
    (logging.WARNING, _("warning")),
    (logging.DEBUG, _("debug")),
    (logging.ERROR, _("error")),
    (logging.FATAL, _("fatal")),
)

# Create your models here.
class ErrorBase(models.Model):
    class_name = models.CharField(_("type"), max_length=128, blank=True, null=True, db_index=True)
    level = models.PositiveIntegerField(choices=LOG_LEVELS, default=logging.ERROR, blank=True, db_index=True)
    message = models.TextField()
    traceback = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)