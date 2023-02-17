import os

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

# ================================================================
# user_data = [['Danis', 'Sharipov'], ['Anna','Sharipova']]

# print()
# x = input("Введите данные для поиска: ")

# for user in user_data:
#     for data in user:
#         if x in data:
#             print(user)

# ===================================================================
# os.system('cs||clear')

# def f(x):
#     a = x*x
#     return a

# user_data = int(input())
# square = f
# os.system('cs||clear')

# print()
# print('Квадрат введеного числа: ',square(user_data))

# exit_porgramm = input()
# os.system('cs||clear')

# ===================================================

# def calc_1(a):
#     return a + a

# def calc_2(b):
#     return b*b

# def lmbd(op, x):
#     print(op(x))

# lmbd(calc_2, 100)

# ===================================================

# def calc_2(a, b):
#     return b*b

# def lmbd(func, a, b):
#     print(func(a, b))

# calc_1 = lambda a,b: a + b

# lmbd(calc_1,5,5)

# ===================================================

# my_list = [1,2,3,5,8,15,23,38]
 #========================================= сам решил
# square = lambda a: a * a

# new_list = [square(i) for i in my_list if i % 2 == 0]

# print()
# print(new_list)

 #========================================= надо было
# my_list = [1,2,3,5,8,15,23,38]
# res = list()

# for i in my_list:
#     if i % 2 == 0:
#         res.append((i, i*i))

# print(res)

# my_list = [1,2,3,5,8,15,23,38]

# def select(func, array):
#     return [func(i) for i in array]

# def where(f, col):
#     return [x for x in col if f(x)]

# res = select(int, my_list)
# print(res)
# res = where (lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)

# x = lambda i: i*i

# result = select(x, my_list)
# print(result)
#=======================================================

# list_1 = [i for i in range(1,5)]

# list_1 = list(map(lambda x: x + 10, list_1))

# print(list_1)

# ======================================================

# data = '123 12 3123 12 312 312 3'

# data = list(map(int, data.split()))

# print()
# print(data)

# data = [12,123,125,125,12,15,]

# res = list(filter(lambda x: x % 10 == 5, data))

# print(res)