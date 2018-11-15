##Celery用法示例

###注意事项
1. celery在使用前需要配置中间人，推荐RabbitMQ，Redis也可以
2. 消息序列化方式如果使用msgpack，需要安装msgpack-python依赖

###Docker启动RabbitMQ

docker run -d --hostname localhost --name docker-rabbit -p 15672:15672 -p 5672:5672 rabbitmq:3.6.15-management

###proj
celery最基础的用法

celery.py中的app是celery实例

启动celery worker命令

celery -A proj worker -l info


###projq
celery中指定队列

在配置文件中定义任务队列，并根据路由键使指定任务进入指定队列

以指定队列的方式启动消费者进程

celery -A projq worker -Q web_tasks -l info


###projb
celery中使用任务调度

在配置文件中设置定时任务

然后启动beat程序和消费者进程

celery beat -A projb

celery -A projb worker -l info

注：Beat和Worker进程可以一并启动：

celery -B -A projb worker -l info


###任务绑定、记录日志和重试

proj中tasks.py的div函数


##pika操作RabbitMQ
rabbit_pika是直接使用Python的第三方package pika 操作RabbitMQ
###核心编程模型
1. 发送者（生产者） 向队列中发送消息
2. 接受者          从队列中接收消息
3. 队列            消息传输的通道，可以有多个

以上三个应用可以不在同一个服务器上