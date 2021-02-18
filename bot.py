import time
import telebot
import os
from pytube import YouTube
from id_user import UserID
from instagram import Insta, instafoto
from ip import IP
from geradorpessoa import gerarPessoa
from gercnpj import GeradorCNPJ

tk = "TOKEN DO SEU BOT"

bot = telebot.TeleBot(tk, parse_mode="markdown")


@bot.message_handler(commands=['start', 'help', 'comesar', 'acorda'])
def welcome(message):
    bot.reply_to(message, '*Olá, sou um bot feito em Python criado pelo @NearShelby_yt tenho varias funções porem a mais usada é a /yt, esse comando baixa o video que você desejar e te manda \n\nObs: Videos longos demoram muito para baixar ou as vezes nem baixam\n\n basta digitar o comando /yt url*\n\n_Exemplo:_\n\n/yt `https://www.youtube.com/watch?v=iJ_pigL5-Lo`\n\n*Outros comandos:*\n\n/criador\n/apis\n/dpwb\n/lokicpf\n/id\n/insta\n/ip\n/gerarpessoa\n/gercnpj')

@bot.message_handler(commands=['criador'])
def ns(message):
    bot.reply_to(message, '*GitHub:* `https://github.com/nearshelby-yt`\n*Youtube:* `https://www.youtube.com/channel/UCYx02EM3e2h2Nbn2OwJ9voQ`\n')

@bot.message_handler(commands=['apis'])
def apis(message):
    bot.reply_to(message, '*Algumas apis:*\n\nhttps://api.hashify.net/hash/md5/hex?value=aquificaoquedesejacodificar \n\nhttps://api.hashify.net/hash/md4/hex?value=aquificaoquedesejacodificar\n\nhttps://viacep.com.br/ws/01001000/json/\n\nhttps://www.receitaws.com.br/v1/cnpj/ \n\nhttp://ip-api.com/json/ \n\nhttp://104.41.5.41:12345/cpf.php?lista={} \n\nhttps://binlist.io/lookup/450570/\n\nhttps://ipwhois.app\n\nhttps://github.com/100n0m3/API-Carros')

@bot.message_handler(commands=['dpwb'])
def deepweb(message):
    bot.reply_to(message, '*Alguns links da deep web*\n\n`http://sigaintbulkwy2vl.onion/\n\nhttp://hiddenchaty5hhgj.onion/\n\nhttp://hss3uro2hsxfogfq.onion/\n\nhttp://hi2vavcolvubv6an.onion/\n\nhttp://highkorea5ou4wcy.onion/\n\nhttp://ippxb64tbjxzltkf.onion/`')

@bot.message_handler(commands=['lokicpf'])
def lokicpf(message):
    bot.reply_to(message, '*Comandos para instalar o LokiCpf que é uma tool de consultar cpf feita em Python pelo NearShelby*\n\n\n*Debian|Ubunto e derivados*\n\napt install git\n\napt install python && apt install python3\n\napt install python-pip3\n\ngit clone https://github.com/nearshelby-yt/LokiCpf\n\ncd LokiCpf\n\npip3 install -r requirements.txt\n\npython3 main.py\n\n\n*Termux*\n\napt install git\n\napt install python && apt install python2\n\ngit clone https://github.com/nearshelby-yt/LokiCpf\n\ncd LokiCpf\n\npip install -r requirements.txt\n\npython3 main.py')

@bot.message_handler(commands=['id'])
def reply(message):

    bot.reply_to(message, UserID(message))

@bot.message_handler(commands=['insta'])
def Instagram(message):

    bot.reply_to(message, Insta(message))
    bot.send_photo(message.chat.id, instafoto(message))

@bot.message_handler(commands=['ip'])
def ConsultaIP(message):

    bot.reply_to(message, IP(message))

@bot.message_handler(commands=['gerarpessoa'])
def GeradorPessoa(message):
    bot.reply_to(message, '*Gerando, aguarde...*')
    bot.reply_to(message, '*Pode demorar um pouco*')
    bot.reply_to(message, gerarPessoa())
    bot.reply_to(message, '*Pessoa gerada, se inscreva no meu canal... digite o comando /criador*')
    
@bot.message_handler(commands=['gercnpj'])
def gerarCNPJ(message):
    
    bot.reply_to(message, GeradorCNPJ(message))
    
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
