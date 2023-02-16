import os
import csv
from modules.book_navigation.menu import *
from modules.book_navigation.close_phonebook import *
from modules.user_operations.new_user import *
from modules.user_operations.find_user import *
from modules.user_operations.show_users import *

def user_show(user_data):
    os.system('cs||clear')
    for user in user_data:
        print(user)
    print()
    menu_return = input("Нажмите Enter ")