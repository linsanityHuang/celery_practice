from datetime import timedelta

# 使用RabbitMQ作为消息代理
BROKER_URL = 'amqp://localhost'

# 使用 amqp 结果后端存储或发送任务的状态
CELERY_RESULT_BACKEND = 'amqp://localhost'

# 任务序列化和反序列化使用msgpack方案
CELERY_TASK_SERIALIZER = 'msgpack'

# 读取任务结果一般性能要求不高，所以使用了可读性更好的JSON
CELERY_RESULT_SERIALIZER = 'json'

# 指定接受的内容类型
CELERY_ACCEPT_CONTENT = ['json', 'msgpack']

# 任务过期时间，不建议直接写86400，应该让这样的magic数字表述更明显
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24

CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_ENABLE_UTC = True

# 新增内容
# CELERYBEAT_SCHEDULE中指定了tasks.add这个任务每10秒跑一次，执行的时候的参数是16和16
CELERYBEAT_SCHEDULE = {
	'add': {
		'task': 'projb.tasks.add',
		'schedule': timedelta(seconds=10),
		'args': (16, 16)
	}
}
