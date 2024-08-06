from rabbitmq_connection import get_connection, get_channel
from message_handler import create_message, send_message, response_callback

from payloads import payload

def main():
    ref = 0
    _url = "http://localhost:3333"
    connection = get_connection()
    channel = get_channel(connection)
    
    _payload = payload(0, ref, connection)
    _endPoint = _payload["endPoint"]
    _methodSend = _payload["methodSend"]
    message = create_message(_methodSend, f"{_url}/{_endPoint}", _payload)
    if (_payload != None): send_message(channel, message)
    
    def on_message_callback(ch, method, properties, body):
        nonlocal ref
        response_id = response_callback(body, channel, connection)
        print(f"Response ID capturado: {response_id}")
        ref += 1
        _payload = payload(response_id, ref, connection)
        if (_payload != None): 
            _endPoint = _payload["endPoint"]
            _methodSend = _payload["methodSend"]
            message = create_message(_methodSend, f"{_url}/{_endPoint}", _payload)
            send_message(channel, message)

    channel.basic_consume(
        queue='response_queue',
        on_message_callback=on_message_callback,
        auto_ack=True
    )

    print('Aguardando resposta. Para sair, pressione CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    main()
