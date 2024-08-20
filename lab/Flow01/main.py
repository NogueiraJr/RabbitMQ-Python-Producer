from rabbitmq_connection import get_connection, get_channel
from message_handler import create_message, send_message, response_callback

from payload_createUser import payloadCreateUser

def main():
    endpoint = "http://localhost:3333"
    connection = get_connection()
    channel = get_channel(connection)
    
    methodSend = "POST"
    message = create_message(methodSend, f"{endpoint}/user", payloadCreateUser)
    send_message(channel, message)
    print("Criando o usuário...")
    
    methodSend = "POST"
    channel.basic_consume(
        queue='response_queue',
        on_message_callback=lambda ch, method, properties, body: response_callback(ch, method, properties, body, channel, connection, methodSend, endpoint),
        auto_ack=True
    )
    
    print('Aguardando resposta. Para sair, pressione CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    main()
