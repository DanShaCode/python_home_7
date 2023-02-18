import os
import csv
from modules.book_navigation.menu import *
from modules.book_navigation.close_phonebook import *
from modules.user_operations.new_user import *
from modules.user_operations.find_user import *
from modules.user_operations.show_users import *
from modules.data_operations.add_data_CSV import *

def load_data_from():
    os.system('cs||clear')
    print()
    src = str(input("Введите относительный путь файла: "))
    with open(src, 'r', encoding='UTF-8') as file:
        user_data = csv.reader(file, delimiter=';')
        user_data = list(user_data)
        print()
        print("Данные загружены")
        print()
        user_await = input("Нажмите Enter")
        user_data.remove(user_data[0])
        return user_data