from paho.mqtt import client as mqtt_client
import random

class ConexaoMQTT:

    broker = 'broker.emqx.io'
    port = 1883
    topic = "grupo02unifei/python/mqtt"
    client_id = f'python-mqtt-{random.randint(0, 100)}'
    username = 'emqx'
    password = 'public'

    def connect_mqtt(self) -> mqtt_client:
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Conectado ao Broker MQTT!")
            else:
                print("Falha na conexão, código retornado: %d\n", rc)
        client = mqtt_client.Client(self.client_id)
        client.username_pw_set(self.username, self.password)
        client.on_connect = on_connect
        client.connect(self.broker, self.port)
        return client