import os
import csv
from modules.book_navigation.menu import *
from modules.book_navigation.close_phonebook import *
from modules.user_operations.new_user import *
from modules.user_operations.find_user import *
from modules.user_operations.show_users import *

def menu(user_data):
    os.system('cs||clear')
    print()
    print("Телефонный справочник")
    print()
    print("(1) Добавить нового пользователя")
    print()
    print("(2) Найти пользователя")
    print()   
    print("(3) Посмотреть список контактов")
    print()
    print("(9) Закрыть справочник")
    print()
    user_input = int(input("Введите в поле соответствующую цифру из меню: "))
    if user_input == 1:
        user_changes = new_user_data(user_data)
        return menu(user_changes)
    if user_input == 2:
        user_search(user_data)
        return menu(user_data)
    if user_input == 3:
        user_show(user_data)
        return menu(user_data)
    if user_input == 9:
        close_phonebook()
    else:
        return menu(user_data)
