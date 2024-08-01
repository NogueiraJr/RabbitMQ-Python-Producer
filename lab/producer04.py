import pika
import json

# Conexão com o RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declarar a fila
channel.queue_declare(queue='user_queue')

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
                      body=json.dumps(message))

print("Mensagem enviada com sucesso!")

# Fechar a conexão
connection.close()
