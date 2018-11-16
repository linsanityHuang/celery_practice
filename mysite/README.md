#Celery With Django

##先决条件
1. celery==4.2.1
2. Django==2.1.2
3. 基本的Django项目

##整合步骤
###1.创建Django项目

1. django-admin startproject mysite
2. 在setting.py中添加celery配置选项，例如：

`
CELERY_BROKER_URL = 'amqp://localhost'
CELERY_RESULT_BACKEND = 'amqp://localhost'
CELERY_TASK_SERIALIZER = 'msgpack'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json', 'msgpack']
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_ENABLE_UTC = True
`
3. 创建mysite/mysite/celery.py文件，目的是提供celery实例

4. 修改mysite/mysite/`__init__`.py文件

5. 然后创建app1应用，创建tasks.py文件，并添加任务

6. 在setting.py文件中注册app1应用

7. 进入项目根目录，也就是manage.py所在的路径下，执行celery -A mysite worker -l info

8. 进入Django的交互式环境python manage.py shell，测试app1.tasks中的任务