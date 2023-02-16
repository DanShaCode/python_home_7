import os
import time
from modules.menu import *
from modules.new_user import *
from modules.show_users import *

def new_user_data(user_data):
    os.system('cs||clear')
    print()
    
    user_info = []

    uniqe_id  = len(user_data) + 1
    user_info.append(uniqe_id)

    user_first = input("Введите Ваше Имя: ")
    user_info.append(user_first)
 
    print()
    user_second = input("Введите Вашу Фамилию: ")
    user_info.append(user_second)
    print()

    user_tel = input("Введите Ваш телефон: ")
    user_info.append(user_tel)
    print()

    user_mail = input("Введите Ваш е-mail: ")
    user_info.append(user_mail)
    print()

    user_data.append(user_info)

    print("Нажмите Enter для возврата в Меню ")
    return user_data
