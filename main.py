import requests
import time
import json
import os


class TelegramBot:
    def __init__(self):
        token = '1757623242:AAFmWYlIyTfugtWHVj1gksmvpTH5k76yaL4'
        self.url_base = f'https://api.telegram.org/bot{token}/'

    def Iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obter_novas_mensagens(update_id)
            dados = atualizacao["result"]
            if dados:
                for dado in dados:
                    update_id = dado['update_id']
                    mensagem = str(dado["message"]["text"])
                    chat_id = dado["message"]["from"]["id"]
                    eh_primeira_mensagem = int(
                        dado["message"]["message_id"]) == 1
                    resposta = self.criar_resposta(
                        mensagem, eh_primeira_mensagem)
                    self.responder(resposta, chat_id)

    # Obter mensagens
    def obter_novas_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)

    # Criar uma resposta
    def criar_resposta(self, mensagem, eh_primeira_mensagem):
        if eh_primeira_mensagem == True or mensagem in ('menu', 'Menu'):
            return f'''Olá, seja bem vindo(a) ao meu portfólio! Digite o número da informação que gostaria de visualizar:{os.linesep}1-Visualizar currículo {os.linesep}2-Visualizar Linkedin {os.linesep}3-Visualizar repertório GitHub'''
        if mensagem == '1':
            return f'Site'
        elif mensagem == '2':
            return f'Site'
        elif mensagem == '3':
            return f'Site' 
        else:
            return 'Gostaria de acessar novamente o menu? Digite "menu"'

    # Responder
    def responder(self, resposta, chat_id):
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao)


bot = TelegramBot()
bot.Iniciar()
