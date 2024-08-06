import pika
import json

def create_message(method, endpoint, payload):
    return {
        "method": method,
        "endpoint": endpoint,
        "headers": {
            "Content-Type": "application/json"
        },
        "payload": payload["payload"]
    }

def send_message(channel, message):
    channel.basic_publish(
        exchange='',
        routing_key='user_queue',
        properties=pika.BasicProperties(
            reply_to='response_queue'
        ),
        body=json.dumps(message)
    )

def response_callback(body, channel, connection):
    print("Resposta recebida: %r" % body.decode('utf-8'))
    
    response_message = json.loads(body.decode('utf-8'))
    text = response_message.get('text')
    
    if text:
        parsed_text = json.loads(text)
        response_id = parsed_text.get('id')
        
        if response_id:
            print(f"ID recebido: {response_id}")
            # connection.close()
            return response_id
