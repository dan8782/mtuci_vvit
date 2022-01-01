import telebot

from utils.config import TOKEN
from commands.timetable import timetable

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота')
    bot.send_message(message.chat.id, 'Выберите день', reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def rasp(message):
    if (message.text.split()[0] in ["Эта_неделя",'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Cуббота']):
        print(message.text.split()[0])
        rasp = timetable(message=message.text)
        bot.send_message(message.chat.id, rasp)
    elif (message.text.split()[0] == 'help'):
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота')
        text = """
sadasd
        """
        bot.send_message(message.chat.id, text, reply_markup=keyboard)

@bot.message_handler(commands=["help"])
def help(message):

    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота')
    text = """
помощь
    """
    bot.send_message(message.chat.id, 'lol', reply_markup=keyboard)

bot.infinity_polling()
