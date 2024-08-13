import pika
import json
import uuid

def connect_to_rabbitmq():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    return connection, channel

def declare_queues(channel):
    channel.queue_declare(queue='user_queue')
    channel.queue_declare(queue='response_queue')
    channel.queue_declare(queue='new_message_queue')

def generate_correlation_id():
    return str(uuid.uuid4())

def create_message():
    return {
        "method": "POST",  # Pode ser "POST", "GET", "DELETE", etc.
        "endpoint": "http://localhost:3333/user",
        "headers": {
            "Content-Type": "application/json"
        },
        "payload": {
            "name": "Ciclano",
            "usr": "usrCiclanoComSenha3",
            "psw": "SenhaDoCiclano3",
            "emails": [
                {
                    "email": "endereco@email.com",
                    "userId": "idAdmin000",
                    "userEmailTypeId": "others",
                    "active": True
                },
                {
                    "email": "endereco2@email.com",
                    "userId": "idAdmin000",
                    "userEmailTypeId": "others",
                    "active": True
                }
            ],
            "phones": [
                {
                    "phone": "12489156131",
                    "userId": "idAdmin000",
                    "userPhoneTypeId": "others",
                    "active": True
                },
                {
                    "phone": "1248915613123465",
                    "userId": "idAdmin000",
                    "userPhoneTypeId": "others",
                    "active": True
                }
            ],
            "userTypeId": "admin"
        }
    }

def send_message(channel, message, correlation_id):
    channel.basic_publish(
        exchange='',
        routing_key='user_queue',
        properties=pika.BasicProperties(
            reply_to='response_queue',
            correlation_id=correlation_id
        ),
        body=json.dumps(message)
    )
    print("Mensagem enviada com sucesso!")

def response_callback(ch, method, properties, body, connection, channel, correlation_id):
    if properties.correlation_id == correlation_id:
        print("Resposta recebida: %r" % body)
        
        # Parse da mensagem
        response_message = json.loads(body)
        
        # Obter o ID da resposta
        response_id = response_message.get('id')
        
        if response_id:
            print(f"ID recebido: {response_id}")
            
            # Criar uma nova mensagem para enviar
            new_message = {
                "method": "POST",
                "endpoint": "http://localhost:3333/new-endpoint",
                "headers": {
                    "Content-Type": "application/json"
                },
                "payload": {
                    "id": response_id,
                    "additional_data": "example_data"
                }
            }

            # Enviar a nova mensagem para a fila
            channel.basic_publish(
                exchange='',
                routing_key='new_message_queue',
                body=json.dumps(new_message)
            )
            print("Nova mensagem enviada com sucesso!")

        # Fechar a conexão após receber a resposta
        connection.close()

def main():
    connection, channel = connect_to_rabbitmq()
    declare_queues(channel)
    correlation_id = generate_correlation_id()
    message = create_message()
    send_message(channel, message, correlation_id)
    
    channel.basic_consume(
        queue='response_queue', 
        on_message_callback=lambda ch, method, properties, body: response_callback(ch, method, properties, body, connection, channel, correlation_id),
        auto_ack=True
    )

    print('Aguardando resposta. Para sair, pressione CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    main()
