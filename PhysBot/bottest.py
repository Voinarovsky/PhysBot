import telebot
from telebot import types
import datetime


schedule = [[[['Нечетная неделя', 'Понедельник:', '2-3 пара, 10:00-13:10: Физика-практика, ауд.2530', '4 пара, 13:30-15:00: Линал-практика, ауд.2433'],   #нечетная неделя 3100
              ['Нечетная неделя', 'Вторник:', '2-3 пара, 10:00-13:10: Матан-лекция, ауд.2433', '4-5 пара, 13:30-16:50: Матан-практика, ауд.2531'],
              ['Нечетная неделя', 'Среда:', 'Нет пар! (Если у тебя нет общеуниверситетских предметов)'],
              ['Нечетная неделя', 'Четверг:', 'История по индивидуальному расписанию'],
              ['Нечетная неделя', 'Пятница:', '2 пара, 10:00-11:30: Soft Skills, ауд.1224в', '4 пара, 13:30-15:00: Линал-лекция, ауд.1122', '5-6 пара, 15:20-18:30: Физика-лабы, ауд.4304'],
              ['Нечетная неделя', 'Суббота:', '1-2 пара, 8:20-11:30: Физика-лекция, ауд.2530']]
                ,[['Нечетная неделя', 'Понедельник:', '2-3 пара, 10:00-13:10: Линал-практика, ауд.2424'],    #нечетная неделя 3142
                  ['Нечетная неделя', 'Вторник:', '2-3 пара, 10:00-13:10: Матан-практика, ауд.1512', '4-5 пара, 13:30-16:50: Матан-лекция, ауд.2530'],
                  ['Нечетная неделя', 'Среда:', '4-5 пара, 13:30-16:50: Физика-лабы, ауд.4304'],
                  ['Нечетная неделя', 'Четверг:', 'История по индивидуальному расписанию'],
                  ['Нечетная неделя', 'Пятница:', '2 пара, 10:00-11:30: Soft Skills, ауд.1224в', '4 пара, 13:30-15:00: Линал-лекция, ауд.1122', '5-6 пара, 15:20-18:30: Физика-практика, ауд.2530'],
                  ['Нечетная неделя', 'Суббота:', '1-2 пара, 8:20-11:30: Физика-лекция, ауд.2530', '3-4 пара, 11:40-15:00: Физхим-лабы, ауд.2313']],
             [['Нечетная неделя', 'Понедельник:', '2-3 пара, 10:00-13:10: Физика-практика, ауд.2433', '4-5 пара, 13:30-16:50: Физика-лабы, ауд.4304'],    #нечетная неделя 3143
              ['Нечетная неделя', 'Вторник:', '2-3 пара, 10:00-13:10: Матан-практика, ауд.2531', '4-5 пара, 13:30-16:50: Матан-лекция, ауд.2530'],
              ['Нечетная неделя', 'Среда:', 'Нет пар! (Если у тебя нет общеуниверситетских предметов)'],
              ['Нечетная неделя', 'Четверг:', 'История по индивидуальному расписанию'],
              ['Нечетная неделя', 'Пятница:', '2 пара, 10:00-11:30: Soft Skills, ауд.1224в', '4 пара, 13:30-15:00: Линал-лекция, ауд.1122', '5-6 пара, 15:20-18:30: Линал-практика, ауд.4207'],
              ['Нечетная неделя', 'Суббота:', '1-2 пара, 8:20-11:30: Физика-лекция, ауд.2530']],
             [['Нечетная неделя', 'Понедельник:', '1-2 пара, 8:20-11:30: Физхим-лабы, ауд.2313'],    #нечетная неделя 3144
              ['Нечетная неделя', 'Вторник:', '2-3 пара, 10:00-13:10: Матан-практика, ауд.2424', '4-5 пара, 13:30-16:50: Матан-лекция, ауд.2530'],
              ['Нечетная неделя', 'Среда:', '2-3 пара, 10:00-13:10: Линал-практика, ауд.2424', '4-5 пара, 13:30-16:50: Физика-практика, ауд.2433'],
              ['Нечетная неделя', 'Четверг:', 'История по индивидуальному расписанию'],
              ['Нечетная неделя', 'Пятница:', '2 пара, 10:00-11:30: Soft Skills, ауд.1224в', '4 пара, 13:30-15:00: Линал-лекция, ауд.1122'],
              ['Нечетная неделя', 'Суббота:', '1-2 пара, 8:20-11:30: Физика-лекция, ауд.2530', '3-4 пара, 11:40-15:00: Физика-лабы, ауд.4304']]],
            [[[['Четная неделя', 'Понедельник:', '2-3 пара, 10:00-13:10: Физика-практика, ауд.2530', '4-5 пара, 13:30-16:50: Линал-практика, ауд.2433'],    #четная неделя 3100
               ['Четная неделя', 'Вторник:', '2-3 пара, 10:00-13:10: Матан-лекция, ауд.2433', '4-5 пара, 13:30-16:50: Матан-практика, ауд.2531'],
               ['Четная неделя', 'Среда:', '2-3 пара, 9:00-12:00: Программирование, ауд.2530'],
               ['Четная неделя', 'Четверг:', '3-4 пара, 11:40-15:00: Физхим-лекция, ауд.1223'],
               ['Четная неделя', 'Пятница:', '2 пара, 10:00-11:30: Soft Skills, ауд.1224в', '3-4 пара, 11:40-15:00: Линал-лекция, ауд.1122', '5-6 пара, 15:20-18:30: Физика-лабы, ауд.4304'],
               ['Четная неделя', 'Суббота:', '1-2 пара, 8:20-11:30: Физика-лекция, ауд.2530', '3-4 пара, 11:40-15:00: Физхим-лабы, ауд.2313']],
              [['Четная неделя', 'Понедельник:', '3 пара, 11:40-13:10: Линал-практика, ауд.2424'],    #четная неделя 3142
               ['Четная неделя', 'Вторник:', '2-3 пара, 10:00-13:10: Матан-практика, ауд.1512', '4-5 пара, 13:30-16:50: Матан-лекция, ауд.2530'],
               ['Четная неделя', 'Среда:', '2-3 пара, 9:00-12:00: Программирование, ауд.2530', '4-5 пара, 13:30-16:50: Физика-лабы, ауд.4304'],
               ['Четная неделя', 'Четверг:', '3-4 пара, 11:40-15:00: Физхим-лекция, ауд.1223'],
               ['Четная неделя', 'Пятница:', '2 пара, 10:00-11:30: Soft Skills, ауд.1224в', '3-4 пара, 11:40-15:00: Линал-лекция, ауд.1122', '5-6 пара, 15:20-18:30: Физика-практика, ауд.2530'],
               ['Четная неделя', 'Суббота:', '1-2 пара, 8:20-11:30: Физика-лекция, ауд.2530']],
              [['Четная неделя', 'Понедельник:', '2-3 пара, 10:00-13:10: Физика-практика, ауд.2433', '4-5 пара, 13:30-16:50: Физика-лабы, ауд.4304'],    #четная неделя 3143
               ['Четная неделя', 'Вторник:', '2-3 пара, 10:00-13:10: Матан-практика, ауд.2531', '4-5 пара, 13:30-16:50: Матан-лекция, ауд.2530'],
               ['Четная неделя', 'Среда:', '2-3 пара, 9:00-12:00: Программирование, ауд.2530'],
               ['Четная неделя', 'Четверг:', '5-6 пара, 15:20-18:30: Физхим-лабы, ауд.2313'],
               ['Четная неделя', 'Пятница:', '2 пара, 10:00-11:30: Soft Skills, ауд.1224в', '3-4 пара, 11:40-15:00: Линал-лекция, ауд.1122', '5 пара, 15:20-16:50: Линал-практика, ауд.4207'],
               ['Четная неделя', 'Суббота:', '1-2 пара, 8:20-11:30: Физика-лекция, ауд.2530']],
              [['Четная неделя', 'Понедельник:', 'Нет пар! (Если у тебя нет общеуниверситетских предметов)'],    #четная неделя 3144
               ['Четная неделя', 'Вторник:', '2-3 пара, 10:00-13:10: Матан-практика, ауд.2424', '4-5 пара, 13:30-16:50: Матан-лекция, ауд.2530'],
               ['Четная неделя', 'Среда:', '2-3 пара, 9:00-12:00: Программирование, ауд.2530', '4-5 пара, 13:30-16:50: Физика-практика, ауд.2433'],
               ['Четная неделя', 'Четверг:', '2 пара, 10:00-11:30: Линал-практика, ауд.2530', '3-4 пара, 11:40-15:00: Физхим-лекция, ауд.1223'],
               ['Четная неделя', 'Пятница:', '2 пара, 10:00-11:30: Soft Skills, ауд.1224в', '3-4 пара, 11:40-15:00: Линал-лекция, ауд.1122'],
               ['Четная неделя', 'Суббота:', '1-2 пара, 8:20-11:30: Физика-лекция, ауд.2530', '3-4 пара, 11:40-15:00: Физика-лабы, ауд.4304']]]]]
#первый подсписок - это нечетная неделя, второй - четная. Далее группы в таком порядке: 3100,3142,3143,3144 и дни недели пн-сб




bot = telebot.TeleBot('5864360081:AAFVfH3fXLHk2mo08pTMJGNIr4zsoOQntvo')

#добавляю 3 главные кнопки в первом меню
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width=1)
    item1 = types.KeyboardButton('🌐 Сервисы ИТМО')
    item2 = types.KeyboardButton('📅 Расписание')

    markup.add(item1, item2)

    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}! Что тебя интересует?'.format(message.from_user), reply_markup = markup) #вывод при старте привет имя



#подменю
@bot.message_handler(content_types=['text'])
def bot_message(message):
    global nowdate
    global gr
    global week_number
    if message.chat.type == 'private':
        if message.text == '📅 Расписание':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('Z3143')
            item2 = types.KeyboardButton('Z3144')
            item3 = types.KeyboardButton('Z3142')
            item4 = types.KeyboardButton('Z3100')
            menu = types.KeyboardButton('⚪ Меню')
            markup.add(item1, item2, item3, item4, menu)
            bot.send_message(message.chat.id, 'Выбери свою группу', parse_mode='html', reply_markup=markup)

        elif message.text == '↩ Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('Z3143')
            item2 = types.KeyboardButton('Z3144')
            item3 = types.KeyboardButton('Z3142')
            item4 = types.KeyboardButton('Z3100')
            menu = types.KeyboardButton('⚪ Меню')
            markup.add(item1, item2, item3, item4, menu)
            bot.send_message(message.chat.id, 'Выбери свою группу', parse_mode='html',reply_markup=markup)

        elif message.text == 'Z3143':
            gr = 2
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('Сегодня')
            item2 = types.KeyboardButton('Завтра')
            back = types.KeyboardButton('↩ Назад')
            markup.add(item1, item2, back)
            bot.send_message(message.chat.id, 'Выбери день', parse_mode='html',reply_markup=markup)

        elif message.text == 'Z3144':
            gr = 3
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('Сегодня')
            item2 = types.KeyboardButton('Завтра')
            back = types.KeyboardButton('↩ Назад')
            markup.add(item1, item2, back)
            bot.send_message(message.chat.id, 'Выбери день', parse_mode='html',reply_markup=markup)

        elif message.text == 'Z3142':
            gr = 1
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('Сегодня')
            item2 = types.KeyboardButton('Завтра')
            back = types.KeyboardButton('↩ Назад')
            markup.add(item1, item2, back)
            bot.send_message(message.chat.id, 'Выбери день', parse_mode='html',reply_markup=markup)

        elif message.text == 'Z3100':
            gr = 0
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('Сегодня')
            item2 = types.KeyboardButton('Завтра')
            back = types.KeyboardButton('↩ Назад')
            markup.add(item1, item2, back)
            bot.send_message(message.chat.id, 'Выбери день', parse_mode='html',reply_markup=markup)

        elif message.text == 'Сегодня':
            nowdate = datetime.datetime.today().weekday()
            week_number = (datetime.datetime.today().isocalendar().week + 1) % 2
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('Сегодня')
            item2 = types.KeyboardButton('Завтра')
            back = types.KeyboardButton('↩ Назад')
            markup.add(item1, item2, back)
            res = "\n".join([f"{item}" for item in schedule[week_number][gr][nowdate]])
            if nowdate == 6:
                bot.send_message(message.chat.id, 'Сегодня нет пар!', parse_mode='html', reply_markup=markup)
            else:
                bot.send_message(message.chat.id, res, parse_mode='html',reply_markup=markup)

        elif message.text == 'Завтра':
            nowdate = (datetime.datetime.today().weekday() + 1) % 7
            week_number = (datetime.datetime.today().isocalendar().week + 1) % 2
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            item1 = types.KeyboardButton('Сегодня')
            item2 = types.KeyboardButton('Завтра')
            back = types.KeyboardButton('↩ Назад')
            markup.add(item1, item2, back)
            res = "\n".join([f"{item}" for item in schedule[week_number][gr][nowdate]])
            if nowdate == 6:
                bot.send_message(message.chat.id, 'Сегодня нет пар!', parse_mode='html', reply_markup=markup)
            else:
                bot.send_message(message.chat.id, res, parse_mode='html',reply_markup=markup)

        elif message.text == '🌐 Сервисы ИТМО':  #подменю сервисы итмо
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('❤ Физтех')
            item2 = types.KeyboardButton('💙 ИТМО')
            menu = types.KeyboardButton('⚪ Меню')
            markup.add(item1, item2, menu)

            bot.send_message(message.chat.id, '[ 🌐 Сервисы ИТМО ] <b>Какой сервис тебя интересует?</b>',parse_mode = 'html', reply_markup=markup)  # вывод что выбра

        elif message.text == '⚪ Меню':  # подменю расписание
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            item1 = types.KeyboardButton('🌐 Сервисы ИТМО')
            item2 = types.KeyboardButton('📅 Расписание')

            markup.add(item1, item2,)

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