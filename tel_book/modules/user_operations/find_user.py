import os
import csv
from modules.book_navigation.menu import *
from modules.book_navigation.close_phonebook import *
from modules.user_operations.new_user import *
from modules.user_operations.find_user import *
from modules.user_operations.show_users import *
from modules.data_operations.add_data_CSV import *

def user_search(user_data):
    os.system('cs||clear')
    print()
    find_input = str(input("Введите данные пользователя: "))
    print()
    for user in user_data:
        flag = 0
        for data in user:
            if find_input in data:
                if flag == 0:
                    print(f"ID : {user[0]} | First Name : {user[1]} | Second Name: {user[2]} | Tel : {user[3]} | E-mail: {user[4]} | Adress : {user[5]}")
                flag += 1
                if flag == 1:
                    continue
    print()
    user_await = input("Введите 'q' для возврата в Меню: ")
    if user_await == 'q':
        return user_data
    else:
        return user_data