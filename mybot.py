import importlib
import telebot
from telebot import types
from googletrans import Translator
token = '5104732046:AAFlvyFL-C-w3N0UDbev-UC9Yr-1V6CGTQo'

import sys
importlib.reload(sys)
sys.setdefaultencoding('utf-8')
bot = telebot.TeleBot(token=token)
translator = Translator()

@bot.message_handler(commands=['start'])
def send(message):
    bot.send_message(message.chat.id, 'Я переводчик-бот')



@bot.message_handler(content_types='text')
def send_mess(message):
    print(message.text)
    client_message = translator.translate(message.text, dest='ru').text
    bot.send_message(message.chat.id, client_message)

print('Бот работает...')
bot.infinity_polling()