import telebot

chave_api = '5379007749:AAF78ropPnhjOKPYCEfytyx2nAXsSXJVtFs'

bot = telebot.TeleBot(chave_api)

@bot.message_handler(commands=['pizza'])
def pizza(mensagem):
    bot.send_message(mensagem.chat.id, 'Saindo a pizza para sua casa: Tempo de espera 40min')

@bot.message_handler(commands=['hamburguer'])
def hamburger(mensagem):
    bot.send_message(mensagem.chat.id, 'Saindo o seu pedido: Tempo de espera 30min')

@bot.message_handler(commands=['salada'])
def salada(mensagem):
    bot.send_message(mensagem.chat.id, 'Desculpe, estamos sem salada, clique aqui para iniciar seu pedido: /iniciar')

@bot.message_handler(commands=['japones'])
def japones(mensagem):
    bot.send_message(mensagem.chat.id, 'O seu japa já esta a caminho!! Tempo de espera 30min')

@bot.message_handler(commands=['opcao1'])
def opcao1(mensagem):
    texto = """
    O que você quer pedir? (clique em uma opção)
    /pizza - Pizza
    /hamburguer - Hamburguer
    /salada - Salada 
    /japones - Japonês
    """
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=['opcao2'])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, 'Para enviar uma reclamação, mande um e-mail para reclamacao@gmail.com')

@bot.message_handler(commands=['opcao3'])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Seg á sexta 18:00 as 00:00 \nSáb, Domingo e feriado 18:00 as 1:00")



def verificar(mensagem):
    return True

#decorator
@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item)
    /opcao1 - Fazer um pedido
    /opcao2 - Reclamar de um pedido
    /opcao3 - Horário de funcionamento
    Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)


# lupping infinito que faz o bot estar conversando com o telegram o tempo todo
bot.polling()