#Добавление csv
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@ author Yalushkin Alexey @@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


import csv
import logger

# первичная запись справочника
def write_csv():
    with open('names.csv', 'w', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['first_name', 'contact info']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'first_name': 'иванов', 'contact info': ['иван', '+79003001212', 'электрик']})
        writer.writerow({'first_name': 'сидоров', 'contact info': ['михаил', '+79621201588', 'сантехник']})
        writer.writerow({'first_name': 'карасев', 'contact info': ['карп', '+79198763232', 'нелюбит рыбалку']})

# чтение из файла с удалением лишних заголовков
def read_csv():
    phone_numbers = dict()
    with open('names.csv', encoding='utf-8', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            phone_numbers[row['first_name']]= row['contact info']
        if 'first_name' in phone_numbers:
            phone_numbers.pop('first_name')
        return phone_numbers

# добавление новой записи
def add_note():
    phone_numbers = read_csv()
    key = input("фамилия ")
    if key in phone_numbers:
        print("Такой контакт уже есть.")
    else:
        phone_numbers[key] = [input('имя '), input('№тел '), input('описание ')]
    logger.number_logger(f"Добавляем контакт: {key}")
    return phone_numbers

# запись изменений
def writer_too(phone_numbers):
    with open('names.csv', 'w', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['first_name', 'contact info']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for key in phone_numbers.keys():
            writer.writerow({'first_name': key, 'contact info': phone_numbers[key]})

# удаление контакта
def delete_note_csv():
    key = input('фамилия = ')
    phone_numbers = read_csv()
    phone_numbers.pop(key)
    writer_too(phone_numbers)
    logger.number_logger(f"Удаляем контакт: {key}")

def print_csv():
    phone_numbers = read_csv()
    for key in phone_numbers.keys():
        s = phone_numbers[key].replace("[", "").replace("'", "").replace(',', "").replace("]", "")
        print(key, s)