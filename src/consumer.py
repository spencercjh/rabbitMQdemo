import pika


def consumer():
    # 消费者
    credentials = pika.PlainCredentials(username='guest', password='guest')
    # 连接到rabbit_mq服务器
    connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1', 5672, credentials=credentials))
    channel = connection.channel()

    # 声明消息队列，消息将在这个队列中进行传递。如果队列不存在，则创建
    channel.queue_declare(queue='wzg', durable=True)

    # 定义一个回调函数来处理，这边的回调函数就是将信息打印出来。
    def callback(ch, method, properties, body):
        if 'fun1' in str(body):
            print(" [fun1] Received %r" % str(body) + " \n" + str(ch) + " " + str(method) + " " + str(properties))
        elif 'fun2' in str(body):
            print(" [fun2] Received %r" % str(body) + " \n" + str(ch) + " " + str(method) + " " + str(properties))
        else:
            print(" [other] Received %r" % str(body) + " \n" + str(ch) + " " + str(method) + " " + str(properties))

    # 告诉rabbit_mq使用callback来接收信息
    channel.basic_consume(callback,
                          queue='hello',
                          no_ack=False)
    # no_ack=True表示在回调函数中不需要发送确认标识

    print(' [*] Waiting for messages.')

    # 开始接收信息，并进入阻塞状态，队列里有信息才会调用callback进行处理。按ctrl+c退出。
    channel.start_consuming()


if __name__ == '__main__':
    consumer()
