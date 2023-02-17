import os
import csv
from modules.book_navigation.menu import *
from modules.book_navigation.close_phonebook import *
from modules.user_operations.new_user import *
from modules.user_operations.find_user import *
from modules.user_operations.show_users import *

def create_book_csv(user_data):
    os.system('cs||clear')
    print()
    print("(1) Импортировать данные в CSV")
    print()
    user_input =int(input("Введите соответствующую цифру из Меню: "))
    if user_input == 1:
        id = 'id'
        first_name = 'First Name'
        second_name = 'Second Name'
        tel = 'tel'
        e_mail = 'e-mail'

        with open('phone_book.csv', 'w') as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(
                [id, first_name, second_name, tel, e_mail]
            )

        for user in user_data:
            with open('phone_book.csv', 'a') as file:
                writer = csv.writer(file, delimiter=";")
                writer.writerow(
                    user
                )

        print()
        print("Данные загружены.")
        print()
        clear = input("Нажмите Enter ... ")
        os.system('cs||clear')
        return user_data
    else:
        return user_data