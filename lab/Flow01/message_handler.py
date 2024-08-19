import pika
import json

def create_message(method, endpoint, payload):
    return {
        "method": method,
        "endpoint": endpoint,
        "headers": {
            "Content-Type": "application/json"
        },
        "payload": payload()["payload"]
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

def create_new_message(method, endpoint, response_id):
    return {
        "method": method,
        "endpoint": f"{endpoint}/new-endpoint",
        "headers": {
            "Content-Type": "application/json"
        },
        "payload": {
            "id": response_id,
            "additional_data": "example_data"
        }
    }

def response_callback(ch, method, properties, body, channel, connection, methodSend, endpoint):
    print("Resposta recebida: %r" % body)
    
    response_message = json.loads(body)
    text = response_message.get('text')
    
    if text:
        parsed_text = json.loads(text)
        response_id = parsed_text.get('id')
        
        if response_id:
            print(f"ID recebido: {response_id}")
            
            new_message = create_new_message(methodSend, endpoint, response_id)
            channel.basic_publish(
                exchange='',
                routing_key='new_message_queue',
                body=json.dumps(new_message)
            )
            
            print("Nova mensagem enviada com sucesso!")
    
    connection.close()
