import telebot
from telebot import types

import add_read_write
from searching import search

bot = telebot.TeleBot('token')




@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("1 - посмотреть справочник")
    btn2 = types.KeyboardButton("2 - найти контакт")
    back = types.KeyboardButton("3 - вернуться в главное меню")
    markup.add(btn1, btn2, back)
    bot.send_message(message.chat.id,text="Привет, {0.first_name}! Я  бот для телефонного справочника".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "1 - посмотреть справочник"):
        bot.send_message(message.chat.id, text="Привет! Спасибо, что смотришь справочник!)")
        bot.send_message(chat_id=message.chat.id, text=add_read_write.read_csv())
    elif (message.text == "2 - найти контакт"):
        bot.send_message(message.chat.id, text="Введите фамилию ")


    elif (message.text == "Что я могу?"):
        bot.send_message(message.chat.id, text="Показать справочник")

    elif (message.text == "3 - вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1 - посмотреть справочник")
        btn2 = types.KeyboardButton("2 - найти контакт")
        back = types.KeyboardButton("3 - вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню")
    else:
        bot.send_message(message.chat.id, text=search_text(message))


@bot.message_handler(content_types=['text'])
def search_text(message):
     bot.send_message(message.chat.id, text=search(message.text))


bot.polling(none_stop=True, interval=0)

