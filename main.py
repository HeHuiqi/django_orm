import sys
from pathlib import Path
import django
from django.conf import settings
from django.core.management import execute_from_command_line,call_command

# 当前目录
BASE_DIR = Path('.')
# 配置app
INSTALLED_APPS = [
    'myapp.apps.MyAppConfig'
]
# 配置数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR/'db.sqlite3',
    }
}
# 配置Django
settings.configure(DATABASES=DATABASES,INSTALLED_APPS=INSTALLED_APPS,DEBUG=True)
django.setup()


# 模型一定要在配置之后导入
from myapp.models import Book

def update_db(app_name):
    execute_from_command_line(['','makemigrations',app_name])
    execute_from_command_line(['','migrate',app_name,])
    # call_command('makemigrations',app_name)
    # call_command('migrate',app_name,)


def main():
    if len(sys.argv) > 1:
        print(sys.argv)
        db_op = sys.argv[1]
        if db_op == 'migrate':
            # 注意这里如果配置的了多个app，就要增加参数
            # 如 
            # execute_from_command_line(['','makemigrations',app_name,app_name1,app_name2])
            # execute_from_command_line(['','migrate',app_name,app_name1,app_name2])

            app_name = 'myapp'
            # 执行数据库迁移
            # execute_from_command_line(['','makemigrations',app_name])
            # execute_from_command_line(['','migrate',app_name,])

            # call_command('makemigrations',app_name)
            # call_command('migrate',app_name,)
            update_db(app_name=app_name)
    try:
        bk = Book()
        bk.name = 'Python基础'
        # 保存数据到数据库
        bk.save()

        books =  Book.objects.all()
        for book in books:
            print(book.name)
    except:
        print('first run use `python main.py migrate`')


main()
