import random
import time
from paho.mqtt import client as mqtt_client

broker = 'broker.emqx.io'
port = 1883
topic = "python/mqtt"
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = 'emqx'
password = 'public'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client, msg):
    while True:
        time.sleep(1)
        result = client.publish(topic, msg)
        status = result[0]
        if status == 0:
            print(f"Send message to topic `{topic}` sucessfully ")
        else:
            print(f"Failed to send message to topic {topic}")




if __name__ == '__main__':
    client = connect_mqtt()
    tipo_mensagem = input("Digite o tipo da sua mensagem [calculo, arquivo, texto]: ")
    if tipo_mensagem == 'calculo':
        valor1 = input('Digite o primeiro valor: ')
        valor2 = input('Digite o segundo valor: ')
        operador = input('Digite o operador [*, /, +, -]: ')
        payload = {
            "valor_1": valor1,
            "valor_2": valor2,
            "operador": operador,
        }
        msg = {
            "tipo_mensagem": tipo_mensagem,
            "payload": payload
        }
        publish(client, str(msg))


