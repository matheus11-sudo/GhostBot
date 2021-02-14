import time
import telebot
import os
from pytube import YouTube


tk = "TOKEN DO SEU BOT"

bot = telebot.TeleBot(tk, parse_mode="markdown")


@bot.message_handler(commands=['start', 'help', 'comesar', 'acorda'])
def welcome(message):
    bot.reply_to(message, '*Olá, sou um bot feito em Python criado pelo @NearShelby_yt tenho varias funções porem a mais usada é a /yt, esse comando baixa o video que você desejar e te manda \n\nObs: Videos longos demoram muito para baixar ou as vezes nem baixam\n\n basta digitar o comando /yt url*\n\n_Exemplo:_\n\n/yt `https://www.youtube.com/watch?v=iJ_pigL5-Lo`\n\n*Outros comandos:*\n\n/criador\n/apis\n/dpwb')

@bot.message_handler(commands=['criador'])
def ns(message):
    bot.reply_to(message, '*GitHub:* `https://github.com/nearshelby-yt`\n*Youtube:* `https://www.youtube.com/channel/UCYx02EM3e2h2Nbn2OwJ9voQ`\n')

@bot.message_handler(commands=['apis'])
def apis(message):
    bot.reply_to(message, '*Algumas apis:*\n\nhttps://api.hashify.net/hash/md5/hex?value=aquificaoquedesejacodificar \n\nhttps://api.hashify.net/hash/md4/hex?value=aquificaoquedesejacodificar\n\nhttps://viacep.com.br/ws/01001000/json/\n\nhttps://www.receitaws.com.br/v1/cnpj/ \n\nhttp://ip-api.com/json/ \n\nhttp://104.41.5.41:12345/cpf.php?lista={} \n\nhttps://binlist.io/lookup/450570/\n\nhttps://ipwhois.app\n\nhttps://github.com/100n0m3/API-Carros')

@bot.message_handler(commands=['dpwb'])
def deepweb(message):
    bot.reply_to(message, '*Alguns links da deep web*\n\n`http://sigaintbulkwy2vl.onion/\n\nhttp://hiddenchaty5hhgj.onion/\n\nhttp://hss3uro2hsxfogfq.onion/\n\nhttp://hi2vavcolvubv6an.onion/\n\nhttp://highkorea5ou4wcy.onion/\n\nhttp://ippxb64tbjxzltkf.onion/`')

@bot.message_handler(commands=['yt'])
def download(message):
    bot.reply_to(message, '*Baixando, aguarde...*')
    url = message.text[4:]
    video = YouTube(url).streams.get_highest_resolution().download(skip_existing=False)
    file = open(video, 'rb')

    bot.send_video(message.chat.id, file, timeout=1000)

    file.close()
    os.remove(video)


while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        telebot.logger.error(e)
        time.sleep(15)
