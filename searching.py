# Добавление поиска
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#   author Victoria Burakhina
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

import add_read_write

def search(surname):
    d = add_read_write.read_csv_for_search()
    if surname in d.keys():
        s = d[surname].replace("[", "").replace("'", "").replace(',', "").replace("]", "")
        return str(surname) + " " + str(s)
    else:
        str('Данных нет в списке')



# if __name__ == '__main__':
#     surname = input('Введите фамилию: ')
#     print(search(surname))
