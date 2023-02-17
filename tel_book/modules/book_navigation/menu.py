import os
import csv
from modules.book_navigation.menu import *
from modules.book_navigation.close_phonebook import *
from modules.user_operations.new_user import *
from modules.user_operations.find_user import *
from modules.user_operations.show_users import *
from modules.user_operations.user_chg import *
from modules.data_operations.add_data import *

def menu(user_data):
    os.system('cs||clear')
    print()
    print("  -= Телефонный справочник =-")
    print()
    print("         ОСНОВНОЕ МЕНЮ")
    print()
    print("=================================")
    print()
    print("(1) Добавить новый контакт")
    print()
    print("(2) Изменить контакт")
    print()  
    print("(3) Найти контакт")
    print()   
    print("(4) Посмотреть список контактов")
    print()
    print("(5) Импортировать данные")
    print() 
    print("(9) Закрыть справочник")
    print()
    print('----------------------------------')
    print()
    user_input = int(input("Введите в поле соответствующую цифру из меню: "))
    if user_input == 1:
        user_data = new_user_data(user_data)
        return menu(user_data)
    if user_input == 2:
        user_data = user_change(user_data)
        return menu(user_data)
    if user_input == 3:
        user_data = user_search(user_data)
        return menu(user_data)
    if user_input == 4:
        user_show(user_data)
        return menu(user_data)
    if user_input == 5:
        user_data = create_book_csv(user_data)
        return menu(user_data)
    if user_input == 9:
        close_phonebook()
    else:
        return menu(user_data)
