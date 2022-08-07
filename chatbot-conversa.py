from mailbox import linesep
import os

from matplotlib import lines
# utilizando o os.linesep para fazer a minha quebra de linha

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome}, eu tenho 24 anos :){os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome}, meu hobbie é viajar e ir em restaurantes!!{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome}, eu estudo Python, Power BI e banco de dados, eu amo estudar <3{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome}, com certeza Python!{os.linesep}')
    else:
        print('Digite apenas as opções 1, 2, 3 ou 4')


def start():
    # apresentar o chatbot
    print('Olá! Bem vindo ao meu primeiro Chatbot')
    # pedir o nome
    nome = input('Digite seu nome: ').upper()
    # pedir o email
    email = input('Digite seu e-mail: ')
    # menu de opções
    while True:
        resposta = input(
            f'O que gostaria de saber hoje? {os.linesep}[1] - Quantos anos você tem? {os.linesep}[2] - Qual é o seu hobbie?{os.linesep}[3] - O que você costuma estudar?{os.linesep}[4] - Qual a sua linguagem de programação favorita?{os.linesep}')
    # processar resposta 
        processar_resposta(resposta,nome)

if __name__ == '__main__':
    start()