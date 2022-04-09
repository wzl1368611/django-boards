#!/usr/bin/env python
import os
import sys
# base_path = os.path.dirname(os.path.dirname(__file__))
# print(base_path)
# # path = os.path.join(base_path,'accounts')
# # path2 = os.path.join(base_path,'boards')
# # print(path)
# # print(path2)
# lists = ["D:/2022年度/0328/Development/myproject/myproject"
#          ]
# sys.path.append(lists[0])
# # sys.path.append(lists[1])
# print(sys.path)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
