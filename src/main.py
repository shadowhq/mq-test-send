import os
import pika

mq_host = os.getenv('MQ_HOST', 'localhost')
connection = pika.BlockingConnection(pika.ConnectionParameters(host=mq_host))
channel = connection.channel()

channel.exchange_declare(exchange='shadow',
                         type='topic')

topic = 'test.foo'
message = 'earthquake!'

channel.basic_publish(exchange='shadow',
                      routing_key=topic,
                      body=message)

print ' [x] Sent %r:%r' % (topic, message)
connection.close()
