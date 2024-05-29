import pika
import sys
import os

class connection():
    def __init__(self) -> None:
        print('i')
        credentials = pika.PlainCredentials(username='admin', password='admin', erase_on_connect=True)
        print('ii')
        parameters = pika.ConnectionParameters(host='192.168.85.130', port=5672, virtual_host='admin', credentials=credentials)
        print('iii')
        self.conn = pika.BlockingConnection(parameters)
        print('iiii')
        self.channel = self.conn.channel()

class publisher():
    def __init__(self) -> None:
        conn_obj = connection()
        self.conn = conn_obj.conn
        self.channel = conn_obj.channel
        print('--')
        self.close_conn = lambda conn: conn.close()
        print('---')

    def send_first_message(self):
        '''
        send a message to the queue with default exchange
        cmd: `python pika_test.py r`
        '''
        print(1)
        self.channel.queue_declare(queue='hello')
        print(2)
        self.channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
        print(" [x] Sent 'Hello World!'")
        self.close_conn(self.conn)


class consumer():
    def __init__(self) -> None:
        conn_obj = connection()
        self.conn = conn_obj.conn
        self.channel = conn_obj.channel
        self.callback = lambda ch, method, property, body: print('[x] received %r' %body)

    def receive_first_message(self):
        '''
        receive a message from rabbit mq
        cmd:  `python pika_test.py r`
        '''
        self.channel.queue_declare(queue='hello')
        self.channel.basic_consume(queue='hello', on_message_callback=self.callback, auto_ack=True)
        self.channel.start_consuming()


if __name__ == '__main__':
    try:
        print(sys.argv)
        if sys.argv[1] == 'p':
            publisher().send_first_message()
        else:
            consumer().receive_first_message()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


