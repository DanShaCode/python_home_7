import os
from modules.menu import *
from modules.new_user import *
from modules.show_users import *
from modules.close_phonebook import *

def menu(user_data):
    os.system('cs||clear')
    print()
    print("Телефонный справочник")
    print()
    print("(1) Добавить нового пользователя")
    print()
    print("(2) Посмотреть список контактов")
    print()
    print("(9) Закрыть справочник")
    print()
    user_input = int(input("Введите в поле соответствующую цифру из меню: "))
    if user_input == 1:
        user_changes = new_user_data(user_data)
        return menu(user_changes)
    if user_input == 2:
        user_show(user_data)
        return menu(user_data)
    if user_input == 9:
        close_phonebook()
    else:
        return menu(user_data)
