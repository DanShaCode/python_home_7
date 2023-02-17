import os
import csv
from modules.book_navigation.menu import *
from modules.book_navigation.close_phonebook import *
from modules.user_operations.new_user import *
from modules.user_operations.find_user import *
from modules.user_operations.show_users import *

def user_change(user_data):
    os.system('cs||clear')
    print()
    user_input = str(input("Введите id персоны: "))
    for id in user_data:
        for user_info in id:
            if user_input == id[0]:
                    print()
                    print(id)
                    print()
                    print("Какие изменения вы хотите произвести?")
                    print()
                    print("(1) Изменить Имя")
                    print()
                    print("(2) Изменить Фамилию")
                    print()
                    print("(3) Изменить Телефон")
                    print()
                    print("(4) Изменить e-mail")
                    print()
                    print("(q) Выход из Меню")
                    print()                                        
                    user_input = str(input("Введите соответствующую цифру из Меню: "))
                    if user_input == '1':
                        os.system('cs||clear')
                        print()
                        change = str(input("Введите новое Имя: "))
                        id[1] = change
                        break
                    if user_input == '2':
                        os.system('cs||clear')
                        print()
                        change = str(input("Введите новую Фамилию: "))
                        id[2] = change
                        break
                    if user_input == '3':
                        os.system('cs||clear')
                        print()
                        change = str(input("Введите новый Телефон: "))
                        id[3] = change
                        break
                    if user_input == '4':
                        os.system('cs||clear')
                        print()
                        change = str(input("Введите новый e-mail: "))
                        id[4] = change
                        break
                    if user_input == 'q':
                        return user_data
    print()
    print("Изменения сохранены")
    print()
    user_await = str(input("Введите 'q' для возврата в Меню: "))
    if user_await == 'q':
        return  user_data  