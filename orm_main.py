import sys
from pathlib import Path
import django
from django.conf import settings
from django.core.management import execute_from_command_line

import settings.custom_settings as my_settings

settings.configure(default_settings=my_settings,DEBUG=True)
django.setup()


# 模型一定要在配置之后导入
from myapp.models import Book
if len(sys.argv) > 1:
    print(sys.argv)
    db_op = sys.argv[1]
    if db_op == 'migrate':
        app_name = 'myapp'
        execute_from_command_line(['','makemigrations',app_name])
        execute_from_command_line(['','migrate',app_name,])



try:
    bk = Book()
    bk.name = 'Python基础'
    bk.save()

    books =  Book.objects.all()
    for book in books:
        print(book.name)
except:
    print('first run use `python main.py migrate`')

