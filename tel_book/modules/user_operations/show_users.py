import os
import csv
from modules.book_navigation.menu import *
from modules.book_navigation.close_phonebook import *
from modules.user_operations.new_user import *
from modules.user_operations.find_user import *
from modules.user_operations.show_users import *
from modules.data_operations.add_data_CSV import *

def user_show(user_data):
    os.system('cs||clear')
    print()
    for user in user_data:
        print(f"ID : {user[0]} | First Name : {user[1]} | Second Name: {user[2]} | Tel : {user[3]} | E-mail: {user[4]} | Adress : {user[5]}")
    print()
    menu_return = input("Нажмите Enter ")