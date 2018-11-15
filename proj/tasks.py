from __future__ import absolute_import
from celery.utils.log import get_task_logger
from proj.celery import app

logger = get_task_logger(__name__)


# tasks.py只有一个任务函数add，
# 让它生效的最直接的方法就是添加app.task这个装饰器
@app.task
def add(x, y):
	return x + y


# 任务绑定、记录日志和重试是Celery常用的3个高级属性
# 当使用bind = True后，函数的参数发生变化，多出了参数self（第一个参数），
# 相当于把div变成了一个已绑定的方法，通过self可以获得任务的上下文
@app.task(bind=True)
def div(self, x, y):
	logger.info('Executing task id {0.id}, args: {0.args!r} kwargs: {0.kwargs!r}'.format(self.request))
	try:
		result = x / y
	except ZeroDivisionError as e:
		# 每5秒就会重试一次，一共重试3次（默认重复3次），然后抛出异常
		raise self.retry(exc=e, countdown=5, max_retries=3)
	return result
