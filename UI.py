import searching
import add_read_write
import csv_format_col


def menu():
    add_read_write.write_csv()
    while True:
        z = input(
            "Введите 1 - посмотреть справочник. \nВведите 2 - найти контакт. \nВведите 3 - добавить новый контакт. \nВведите 4 - удалить контакт. \nВведите 5 - вывод в столбец. \nВведите 0 - выход.\n")

        match z:
            case '1':
                add_read_write.print_csv()
                print()
            case '2':
                searching.search()
                print()
            case '3':
                a = add_read_write.add_note()
                add_read_write.writer_too(a)
                print()
            case '4':
                add_read_write.delete_note_csv()
                print()
            case '5':
                csv_format_col.print_csv_col()
                print()
            case '0':
                break





#btn1 = telebot.types.InlineKeyboardButton('действие 1', callback_data='1')
#btn2 = telebot.types.InlineKeyboardButton('действие 2', callback_data='2')

#markup3 = ReplyKeyboardMarkup().add(
   # btn1).add(btn2)



# Готовим кнопки
# keyboard = types.InlineKeyboardMarkup()
# # По очереди готовим текст и обработчик для каждой кнопки
# ty
# key_odin = types.InlineKeyboardButton(text='1', callback_data=add_read_write.print_csv())
# # И добавляем кнопку на экран
# keyboard.add(key_odin)
# key_dva = types.InlineKeyboardButton(text='2', callback_data='option')
# keyboard.searching.search()
# key_tri = types.InlineKeyboardButton(text='3', callback_data='option')
# keyboard.add_read_write.writer_too()
# key_chetire = types.InlineKeyboardButton(text='4', callback_data='option')
# keyboard.add_read_write.delete_note_csv()
# key_piat = types.InlineKeyboardButton(text='5', callback_data='option')
# keyboard.csv_format_col.print_csv_col()
# key_null = types.InlineKeyboardButton(text='0', callback_data='option')
#
# # Показываем все кнопки сразу и пишем сообщение о выборе
# bot.send_message(message.from_user.id, text='Выберите опцию для работы со справочником', reply_markup=keyboard)

#start_markup = telebot.types.InlineKeyboardMarkup()

# первый ряд (две кнопки)
#btn1= telebot.types.InlineKeyboardButton('действие 1', callback_data='1')
#btn2= telebot.types.InlineKeyboardButton('действие 2', callback_data='2')
#start_markup.row(btn1, btn2)

# второй ряд (одна кнопка)
#btn3= telebot.types.InlineKeyboardButton('действие 3', callback_data='3')
#start_markup.row(btn3)

# третий ряд (две кнопки)
#btn4= telebot.types.InlineKeyboardButton('действие 4', callback_data='4')
#btn5= telebot.types.InlineKeyboardButton('действие 5', callback_data='5')
#start_markup.row(btn4, btn5)

# четвертый ряд (две кнопки)
##btn7= telebot.types.InlineKeyboardButton('действие 7', callback_data='7')
#start_markup.row(btn6, btn7)

# пятый ряд (одна кнопка)
#btn8= telebot.types.InlineKeyboardButton('действие 8', callback_data='8')
#start_markup.row(btn8)

