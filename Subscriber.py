
from paho.mqtt import client as mqtt_client
from ConexaoMQTT import ConexaoMQTT

class Subscriber(ConexaoMQTT):

    def __init__(self):
        client = self.connect_mqtt()
        self.run(client)

    def subscribe(self, client: mqtt_client):
        def on_message(client, userdata, msg):
            decodedMessage = msg.payload.decode()
            message = eval(decodedMessage)
            payload = message['payload']
            if message['tipo_mensagem'] == 'calculo':
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
            if message['tipo_mensagem'] == 'texto':
                msg = message['payload']
                print(f"Mensagem recebida: {msg}")
            if message['tipo_mensagem'] == 'arquivo':
                conteudo = message['payload']
                arquivo = open("arquivo.txt", "w+")
                arquivo.write(f"{conteudo}")
                arquivo.close()
                print("Arquivo alterado com sucesso")

        client.subscribe(self.topic)
        client.on_message = on_message

    def run(self, client: mqtt_client):
        self.subscribe(client)
        client.loop_forever()


if __name__ == '__main__':
    Subscriber()