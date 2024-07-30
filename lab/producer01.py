import pika

credentials = pika.PlainCredentials('guest', 'guest')

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials)
)

channel = connection.channel()

channel.exchange_declare(exchange='user_data_exchange', exchange_type='direct')

def send_message(message):
  channel.basic_publish(exchange='user_data_exchange',
                        routing_key='user_data',
                        body=message)

send_message('http://localhost:3333/user/idAdmin000')

connection.close()
