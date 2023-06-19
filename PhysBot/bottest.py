import telebot
from telebot import types
import sqlite3 as sq


__connection = None

def get_connection():
    global __connection
    if __connection is None:
        __connection = sq.connect('data_students')
    return __connection

def init_db(force: bool = False):

    conn = get_connection()
    c = conn.cursor()

    if force:
        c.execute('DROP TABLE IF EXISTS users')

    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id     INTEGER NOT NULL,
            group_id    INTEGER NOT NULL);
    ''')

    conn.commit()

def add_user_id(user_id: int, group_id: int):

    conn = get_connection()
    c = conn.cursor()


    c.execute('INSERT INTO users (user_id, group_id) VALUES (?, ?)', (user_id, group_id))
    conn.commit()
    



bot = telebot.TeleBot('5864360081:AAFVfH3fXLHk2mo08pTMJGNIr4zsoOQntvo')

#добавляю 3 главные кнопки в первом меню
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width=1)
    item1 = types.KeyboardButton('🌐 Сервисы ИТМО')
    item2 = types.KeyboardButton('📅 Расписание')
    item3 = types.KeyboardButton('🔆 Какие сегодня пары?')
    item4 = types.KeyboardButton('База данных')

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}! Что тебя интересует?'.format(message.from_user), reply_markup = markup) #вывод при старте привет имя

groupid = 0
def get_group_id(message):
    global groupid
    groupid = int(message.text)
    if type(groupid) == int:
        bot.send_message(message.chat.id, 'отлично!')
        if __name__ == '__main__':
            init_db()
            add_user_id(int(message.from_user.id), int(groupid))


#подменю
@bot.message_handler(content_types=['text'])
def bot_message(message):
    
    if message.chat.type == 'private':
        if message.text == '🔆 Какие сегодня пары?': #пары сегодня
          markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
          item1 = types.KeyboardButton('⚪ Меню')
          markup.add(item1)

          bot.send_message(message.chat.id, 'У тебя нет пар, тебя отчислили( (а вообще потом пары на сегодня будут)')

        elif message.text == 'База данных':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('⚪ Меню')
            markup.add(item1)
            bot.send_message(message.chat.id, 'Если тебя ещё нет в базе, то пожалуйста напиши номер своей группы! (без буквы z)', parse_mode='html')
            bot.register_next_step_handler(message, get_group_id)

        elif message.text == '🌐 Сервисы ИТМО':  #подменю сервисы итмо
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('❤ Физтех')
            item2 = types.KeyboardButton('💙 ИТМО')
            menu = types.KeyboardButton('⚪ Меню')
            markup.add(item1, item2, menu)

            bot.send_message(message.chat.id, '[ 🌐 Сервисы ИТМО ] <b>Какой сервис тебя интересует?</b>',parse_mode = 'html', reply_markup=markup)  # вывод что выбра

        elif message.text == '📅 Расписание':  # подменю расписание
            bot.send_message(message.chat.id, '[ 📅 Расписание ] <b>Что ты хочешь сделать?</b> (дальше тут функционал расписания)', parse_mode = 'html')  # вывод что выбрал

        elif message.text == '⚪ Меню':  # подменю расписание
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('🌐 Сервисы ИТМО')
            item2 = types.KeyboardButton('📅 Расписание')
            item3 = types.KeyboardButton('🔆 Какие сегодня пары?')

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, f'{message.from_user.first_name}, тебя что-то еще интересует?'.format(message.from_user), reply_markup=markup)  # вывод при старте привет имя

        elif message.text == '💙 ИТМО':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('My.Itmo')
            item2 = types.KeyboardButton('Itmo.Print')
            item3 = types.KeyboardButton('ИСУ ИТМО')
            back = types.KeyboardButton('⤴ Назад')
            menu = types.KeyboardButton('⚪ Меню')

            markup.add(item1, item2, item3, menu, back)

            bot.send_message(message.chat.id, '[ 💙 ИТМО] <b>Какой сервис тебя интересует?</b>',parse_mode='html', reply_markup=markup)  # вывод что выбра

        elif message.text == 'My.Itmo':
            bot.send_message(message.chat.id, 'Сайт My.Itmo : https://my.itmo.ru')

        elif message.text == 'Itmo.Print':
            bot.send_message(message.chat.id, 'Телеграмм-бот Itmo.Print : @ITMO_print_bot ')

        elif message.text == 'ИСУ ИТМО':
            bot.send_message(message.chat.id, 'Сайт ИСУ ИТМО : https://isu.ifmo.ru/pls/apex/f?p=2143:1:104623020831626')

        elif message.text == '⤴ Назад':  #подменю сервисы итмо
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('❤ Физтех')
            item2 = types.KeyboardButton('💙 ИТМО')
            menu = types.KeyboardButton('⚪ Меню')
            markup.add(item1, item2, menu)

            bot.send_message(message.chat.id, '[ 🌐 Сервисы ИТМО ] <b>Какой сервис тебя интересует?</b>',parse_mode = 'html', reply_markup=markup)  # вывод что выбра

        elif message.text == '❤ Физтех':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('Study.Physics')
            item2 = types.KeyboardButton('Новый Физтех')
            item3 = types.KeyboardButton('Забронировать переговорку')
            back = types.KeyboardButton('⤴ Назад')
            menu = types.KeyboardButton('⚪ Меню')

            markup.add(item1, item2, item3, menu, back)

            bot.send_message(message.chat.id, '[ ❤ Физтех ] <b>Какой сервис тебя интересует?</b>', parse_mode='html', reply_markup=markup)  # вывод что выбра

        elif message.text == 'Study.Physics':
            bot.send_message(message.chat.id, 'Сайт Study.Physics : https://study.physics.itmo.ru')

        elif message.text == 'Новый Физтех':
            bot.send_message(message.chat.id, 'Сайт Нового Физтеха : https://physics.itmo.ru/ru ')

        elif message.text == 'Забронировать переговорку':
            bot.send_message(message.chat.id, 'Бот для брони : https://t.me/Phystech_rooms_bot ')


bot.polling(none_stop=True)