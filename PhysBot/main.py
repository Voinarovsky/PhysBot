import telebot
from telebot import types

bot = telebot.TeleBot('5864360081:AAFVfH3fXLHk2mo08pTMJGNIr4zsoOQntvo')

@bot.message_handler(commands=['website'])
def website(message):
    marcup = types.InlineKeyboardMarkup()
    marcup.add(types.InlineKeyboardButton('Сайт My.Itmo', url='https://my.itmo.ru'))
    bot.send_message(message.chat.id, reply_markup=markup)