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


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        decodedMessage = msg.payload.decode()
        if decodedMessage != 'hi deva':
            decodedMessage = eval(decodedMessage)
            payload = decodedMessage['payload']
            if decodedMessage['tipo_mensagem'] == 'calculo':
                valor1 = payload['valor_1']
                valor2 = payload['valor_2']
                operador = payload['operador']
                if operador == '+':
                    resultado = float(valor1) + float(valor2)
                elif operador == '*':
                    resultado = float(valor1) * float(valor2)
                elif operador == '/':
                    resultado = float(valor1) / float(valor2)
                elif operador == '-':
                    resultado = float(valor1) - float(valor2)
            print(f"{valor1} {operador} {valor2} = {resultado}")


    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()