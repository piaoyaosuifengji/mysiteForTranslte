#!/usr/bin/python3
import os
import sys
import logging
# from articleTranlate.views import articleView 


# /home/jty/DjangoPro/mysiteForTranslte/articleTranlate/views.py
logging.basicConfig(filename='example.log', level=logging.DEBUG)


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysiteForTranslte.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
 
 