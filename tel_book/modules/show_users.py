import os
from modules.menu import *
from modules.new_user import *
from modules.show_users import *

def user_show(user_data):
    os.system('cs||clear')
    for user in user_data:
        print(user)
    print()
    menu_return = input("Нажмите Enter ")