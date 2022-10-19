# csv в столбик
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#   author Александр Улитин
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

import csv
import add_read_write

#запись csv в столбец
def write_csv_cols():
    phone_numbers = add_read_write.read_csv()
    with open('note1.csv', 'w', encoding='utf-8', newline='') as file:
        for key in phone_numbers.keys():
            s = phone_numbers[key].replace("[", " ").replace("'", "").replace(',', "").replace("]", "")
            s = s.split()
            #ниже описывается как записать в файл. \n - это новая строка  key
            file.write(f'{key},\n{s[0]}\n{s[1]}\n{s[2]}\n\n')
            


#чтение из csv в столбик  (сам csv тоже в столбик)
def read_csv_col():
    write_csv_cols()
    with open('note1.csv', 'r', encoding='utf-8', newline='') as file:
        readfile = file.read()
        tablo = ("".join(readfile))
        key = tablo[0:tablo.find(',')]
        named = dict()
        named[key] = tablo[tablo.find(',')+2:tablo.find(']')]
        return named

# печать на экран  
def print_csv_col():
    phone_numbers = read_csv_col()
    for key in phone_numbers.keys():
        tmp = phone_numbers[key]
        print(f'{key},\n{tmp}')