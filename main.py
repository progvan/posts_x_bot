import telebot
from telebot import types

import config
import answer
import core

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
   bot.send_message(message.chat.id, answer.TEXT_WELCOME_USERS, reply_markup=types.ReplyKeyboardRemove())

bot.polling(none_stop = True)