import pika
import json
import uuid

# Conexão com o RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declarar as filas
channel.queue_declare(queue='user_queue')
channel.queue_declare(queue='response_queue')

# Função para gerar um ID de correlação único
correlation_id = str(uuid.uuid4())

# Mensagem a ser enviada
message = {
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

# Enviar a mensagem para a fila
channel.basic_publish(exchange='',
                      routing_key='user_queue',
                      properties=pika.BasicProperties(
                          reply_to='response_queue',
                          correlation_id=correlation_id
                      ),
                      body=json.dumps(message))

print("Mensagem enviada com sucesso!")

# Função callback para processar as respostas recebidas
def response_callback(ch, method, properties, body):
    if properties.correlation_id == correlation_id:
        print("Resposta recebida: %r" % body)
        
        # Parse da mensagem
        response_message = json.loads(body)
        
        # Processar a resposta conforme necessário
        print(f"Status Code: {response_message['status_code']}")
        print(f"Response Text: {response_message['text']}")
        
        # Fechar a conexão após receber a resposta
        connection.close()

# Configurar o consumidor para ouvir a fila de respostas
channel.basic_consume(queue='response_queue', on_message_callback=response_callback, auto_ack=True)

print('Aguardando resposta. Para sair, pressione CTRL+C')
channel.start_consuming()
