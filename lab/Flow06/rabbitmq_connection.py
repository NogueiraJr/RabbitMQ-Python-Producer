import pika

def get_connection():
    return pika.BlockingConnection(pika.ConnectionParameters('localhost'))

def get_channel(connection):
    channel = connection.channel()
    channel.queue_declare(queue='user_queue')
    channel.queue_declare(queue='response_queue')
    channel.queue_declare(queue='new_message_queue')
    return channel
