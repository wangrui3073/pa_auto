#!/usr/bin/env python
import os
import sys
# import django
from api_automation_test import settings

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api_automation_test.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

    # os.chdir(settings.BASE_DIR)
    # print(os.getcwd())
    # os.system("celery -A celery_tasks.main worker -l info")
