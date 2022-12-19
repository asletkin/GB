# 1 Задайте список из нескольких чисел. 1 Напишите программу,
# которая найдёт сумму элементов списка,
# стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
lst = [2, 3, 5, 9, 3]


def sum_odd_elem(lst_):
    sum_ = 0
    for i in range(1, len(lst_), 2):
        sum_ += lst_[i]
    return sum_


print(f'Задание 1: {sum_odd_elem(lst)}')

# 2 Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
lst1 = [2, 3, 4, 5, 6]


def lst_f_and_l(lst_):
    new_lst = []
    c = len(lst_) - 1
    for i in range(round((len(lst_) + 1) / 2)):
        new_lst.append(lst_[i] * lst_[c])
        c -= 1
    return new_lst


print(f'Задание 2: {lst_f_and_l(lst1)}')

# 3 Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
lst2 = [1.1, 1.2, 3.1, 5, 10.01]


def difference_max_min(lst_):
    min_ = round(lst_[0] - int(lst_[0]), 2)
    max_ = round(lst_[0] - int(lst_[0]), 2)
    for i in lst_:
        i = round(i - int(i), 2)
        if i != 0:
            if i > max_:
                max_ = i
            if i < min_:
                min_ = i
    return max_ - min_


print(f'Задание 3: {difference_max_min(lst2)}')

# 4 Напишите программу, которая будет преобразовывать десятичное число
# в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10
num = 45


def change_num(num_):
    lst_ = []
    res = ''
    while int(num_):
        lst_.append(num_ % 2)
        num_ = int(num_ / 2)

    for i in lst_[::-1]:
        res += str(i)
    return res


print(f'Задание 4: {int(change_num(num))}')

# 5 Задайте число. Составьте список чисел Фибоначчи, в том числе
# для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
num = 8


def fib(num_):
    num1 = 1
    num2 = 1
    for i in range(2, num_):
        num1, num2 = num2, num1 + num2
    return num2


def neg_fib(num_):
    if num_ == 1:
        return 1
    elif num_ == 2:
        return -1
    else:
        num1 = 1
        num2 = -1
        for i in range(2, num_):
            num1, num2 = num2, num1 - num2
        return num2


lst5 = [0]

for i in range(1, num + 1):
    lst5.append(fib(i))
    lst5.insert(0, neg_fib(i))
print(f'Задание 5: {lst5}')
