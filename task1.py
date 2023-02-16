# 1. В списке хранятся числа. Нужно выбрать только чётные числа и составить
# список пар (число; квадрат числа).

# my_list = [1, 2, 3, 5, 8, 15, 23, 38]

# square = lambda a: a*a
# append_list = []

# for i in my_list:

#     if i % 2 == 0:
#         append_list.append(i)
#         result = square(i)
#         append_list.append(result)

# print()
# print(append_list)


# 2. Функция map =================================

# prod = lambda a: a*2

# my_list = [1,2,3,4,5,6,7,8,9,10]

# my_list = list(map(prod, my_list))

# print()
# print(my_list)

# 3. Функция filter ================================

# my_list = [1,2,3,4,5,6,7,8,9,10]

# odds = []
# odd = lambda a: a % 2 == 0

# my_list = odds.append(list(filter(odd, my_list)))

# print()
# print(odds)

# 4. Функция Zip ==================================

# my_list_numbers = [1,2,3]
# my_list_words = ['a','b','c']

# my_list = list(zip(my_list_numbers, my_list_words))

# print()
# print(my_list)

# 5. Функция enumerate ============================

# my_list = ['Омск','Москва','Абакан','Новосибирск','Питер']

# numerate = list(enumerate(my_list))

# print()
# print(numerate)

# print(numerate[1])

# =============================================================

# id = 'id'
# first_name = 'First Name'
# second_name = 'Second Name'
# tel = 'tel'
# e_mail = 'e-mail'

# with open('tel_book\phone_book.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerow(
#         [id, first_name, second_name, tel, e_mail]
#     )

# user_data = [
# ]

# for user in user_data:
#     with open('tel_book\phone_book.csv', 'a') as file:
#         writer = csv.writer(file)
#         writer.writerow(
#             user
#         )

# print()
# print("Данные загружены.")
# print()
# clear = input("Нажмите Enter ... ")
# os.system('cs||clear')


# list_1 = [1,2,3]
# list_3 = []

# list_3.append(list_1)

# list_2 = [4,5,6]

# list_3.append(list_2)

# print(list_3)