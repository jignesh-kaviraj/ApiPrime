
import logging
import sys
import traceback as traceback_mod
import warnings
from django.utils.encoding import smart_str
from Account.models import ErrorBase
from django.http import HttpResponse
import json
from django.conf import settings
from functools import wraps

def create_from_exception(self, url=None, exception=None, traceback=None, **kwargs):
    if not exception:
        exc_type, exc_value, traceback = sys.exc_info()
    elif not traceback:
        warnings.warn("Using just the ``exception`` argument is deprecated, send ``traceback`` in addition.", DeprecationWarning)
        exc_type, exc_value, traceback = sys.exc_info()
    else:
        exc_type = exception.__class__
        exc_value = exception

    def to_unicode(f):
        if isinstance(f, dict):
            nf = dict()
            for k, v in f.items():
                nf[str(k)] = to_unicode(v)
            f = nf
        elif isinstance(f, (list, tuple)):
            f = [to_unicode(f) for f in f]
        else:
            try:
                f = smart_str(f)
            except (UnicodeEncodeError, UnicodeDecodeError):
                f = "(Error decoding value)"
        return f

    tb_message = "\n".join(traceback_mod.format_exception(exc_type, exc_value, traceback))

    kwargs.setdefault("message", to_unicode(exc_value))
    level = logging.ERROR
    if kwargs.get("level"):
        level = kwargs["level"]

    ErrorBase.objects.create(class_name=exc_type.__name__, message=to_unicode(exc_value), traceback=tb_message, level=level)


def create_from_text(message, class_name=None, level=40, traceback=None):
    ErrorBase.objects.create(class_name=class_name, message=message, traceback=traceback, level=level)


def check_secret_key(function):
    @wraps(function)
    def decorator(request, *args, **kwrgs):
        key = request.headers.get("Secret-Key")
        if key == settings.SECRET_KEY:
            return function(request, *args, **kwrgs)
        else:
          return HttpResponse(json.dumps({"data":{}, "status": 0, "message": "Secret key did not match!"}))

    return decorator