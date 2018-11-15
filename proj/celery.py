# "from __future__ import absolute_import"是拒绝隐式引入，
# 因为celery.py的名字和celery的包名冲突，需要使用这条语句让程序正确地运行
from __future__ import absolute_import
from celery import Celery


# app是Celery类的实例，创建的时候添加了proj.tasks这个模块，
# 也就是包含了proj/tasks.py这个文件
app = Celery('proj', include=['proj.tasks'])

# 把Celery配置存放进proj/celeryconfig.py文件，
# 使用app.config_from_object加载配置
app.config_from_object('proj.celeryconfig')


'''
启动消费者
celery -A proj worker -l info

-A参数默认会寻找proj.celery这个模块，
其实使用celery作为模块文件名字不怎么合理。
可以使用其他名字。

举个例子，假如是proj/app.py，可以使用如下命令启动：
celery -A proj.app worker -l info

'''
if __name__ == '__main__':
	app.start()
