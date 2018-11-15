import pika

# 链接RabbitMQ服务
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 声明队列, 发消息前需要保证队列存在，否则消息会被RabbitMQ丢弃
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
	# print(ch, method, properties)
	print(" [x] Received %r" % body)


channel.basic_consume(callback,
					  queue='hello',
					  no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
