# Добавление поиска
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#   author Victoria Burakhina
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

import add_read_write

def search():
    surname = input('Введите фамилию: ')
    d = add_read_write.read_csv()
    if surname in d.keys():
        s = d[surname].replace("[", "").replace("'", "").replace(',', "").replace("]", "")
        print(surname, s)
    else:
        print('Данных нет в списке')
        print('Выход в общее меню')