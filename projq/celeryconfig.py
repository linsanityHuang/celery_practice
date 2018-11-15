from kombu import Queue

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
CELERY_QUEUES = (  # 定义任务队列
	
	Queue('default', routing_key='task.#'),  # 路由键以“task.”开头的消息都进default队列
	
	Queue('web_tasks', routing_key='web.#'),  # 路由键以“web.”开头的消息都进web_tasks队列

)

CELERY_DEFAULT_EXCHANGE = 'tasks'  # 默认的交换机名字为tasks

CELERY_DEFAULT_EXCHANGE_TYPE = 'topic'  # 默认的交换类型是topic

CELERY_DEFAULT_ROUTING_KEY = 'task.default'  # 默认的路由键是task.default，这个路由键符合上面的default队列

CELERY_ROUTES = {
	
	'projq.tasks.add': {  # tasks.add的消息会进入web_tasks队列
		
		'queue': 'web_tasks',
		
		'routing_key': 'web.add',
		
	}
	
}
