from ConexaoMQTT import ConexaoMQTT

class Publisher(ConexaoMQTT):
    def __init__(self):
        client = self.connect_mqtt()
        self.run(client)

    def run(self, client):
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
            self.publish(client, str(msg))
        if  tipo_mensagem == 'texto':
            texto = input('Digite seu texto: ')
            msg = {
                "tipo_mensagem": tipo_mensagem,
                "payload": texto
            }
            self.publish(client, str(msg))
        if tipo_mensagem == 'arquivo':
            conteudo = input('Digite o novo conteudo do arquivo: ')
            msg = {
                "tipo_mensagem": tipo_mensagem,
                "payload": conteudo
            }
            self.publish(client, str(msg))

    def publish(self, client, msg):
        result = client.publish(self.topic, msg)
        status = result[0]
        if status == 0:
            print(f"Mensagem para o tópico `{self.topic}` enviada com sucesso ")
        else:
            print(f"Falha ao enviar mensagem para o tópico {self.topic}")

if __name__ == '__main__':
    Publisher()