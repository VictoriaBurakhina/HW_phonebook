# Menu
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#   author Zukhra
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

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
