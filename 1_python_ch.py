# Р—Р°РґР°РЅРёРµ 1 РќР°РїРёС€РёС‚Рµ РїСЂРѕРіСЂР°РјРјСѓ, РєРѕС‚РѕСЂР°СЏ РїСЂРёРЅРёРјР°РµС‚ РЅР° РІС…РѕРґ РІРµС‰РµСЃС‚РІРµРЅРЅРѕРµ С‡РёСЃР»Рѕ
# Рё РїРѕРєР°Р·С‹РІР°РµС‚ СЃСѓРјРјСѓ РµРіРѕ С†РёС„СЂ.
# РџСЂРёРјРµСЂ:
# 6782 -> 23
# 0,56 -> 11


def sum_digits(num):
    sum = 0
    for i in range(len(num)):
        if num[i].isdigit():
            sum += int(num[i])
    return f'{num} -> {sum}'

print(sum_digits(input('num: ')))


# Р—Р°РґР°РЅРёРµ 2 РќР°РїРёС€РёС‚Рµ РїСЂРѕРіСЂР°РјРјСѓ, РєРѕС‚РѕСЂР°СЏ РїСЂРёРЅРёРјР°РµС‚ РЅР° РІС…РѕРґ С‡РёСЃР»Рѕ N
# Рё РІС‹РґР°РµС‚ РЅР°Р±РѕСЂ РїСЂРѕРёР·РІРµРґРµРЅРёР№ С‡РёСЃРµР» РѕС‚ 1 РґРѕ N.
# РџСЂРёРјРµСЂ: РїСѓСЃС‚СЊ N = 4, С‚РѕРіРґР° [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def mult_numbers(N):
    lst = []
    count = 1
    for i in range(count, N + 1):
        lst.append(count)
        count = lst[i - 1] * (i + 1)
    return lst

print(mult_numbers(int(input('N: '))))


# Р—Р°РґР°РЅРёРµ 3 Р—Р°РґР°Р№С‚Рµ СЃРїРёСЃРѕРє РёР· n С‡РёСЃРµР» РїРѕСЃР»РµРґРѕРІР°С‚РµР»СЊРЅРѕСЃС‚Рё (1+1/n)^n
# Рё РІС‹РІРµРґРёС‚Рµ РЅР° СЌРєСЂР°РЅ РёС… СЃСѓРјРјСѓ,РѕРєСЂСѓРіР»С‘РЅРЅСѓСЋ РґРѕ С‚СЂС‘С… Р·РЅР°РєРѕРІ РїРѕСЃР»Рµ С‚РѕС‡РєРё.
# РџСЂРёРјРµСЂ: Р”Р»СЏ n = 6 -> 14.072


def sum_numbers_n(n):
    lst = []
    for i in range(1, n + 1):
        lst.append((1 + 1 / i) ** i)
    return '%.3f' % sum(lst)

print(sum_numbers_n(int(input('n: '))))


# 3.1


def sum_numbers_n(n):
    return '%.3f' % sum([(1 + 1 / i) ** i for i in range(1, n+1)])

print(sum_numbers_n(int(input('n: '))))


# Р—Р°РґР°РЅРёРµ 4 Р—Р°РґР°Р№С‚Рµ СЃРїРёСЃРѕРє РёР· N СЌР»РµРјРµРЅС‚РѕРІ, Р·Р°РїРѕР»РЅРµРЅРЅС‹С… С‡РёСЃР»Р°РјРё РёР· РїСЂРѕРјРµР¶СѓС‚РєР° [-N, N].
# РќР°Р№РґРёС‚Рµ РїСЂРѕРёР·РІРµРґРµРЅРёРµ СЌР»РµРјРµРЅС‚РѕРІ РЅР° РїРѕР·РёС†РёСЏС… a Рё b.
# Р—РЅР°С‡РµРЅРёСЏ N, a Рё b РІРІРѕРґРёС‚ РїРѕР»СЊР·РѕРІР°С‚РµР»СЊ СЃ РєР»Р°РІРёР°С‚СѓСЂС‹.


def a_and_b(N, a, b):
    lst = []
    for i in range(N, 0, -1):
        i *= -1
        lst.append(i)
    for i in range(N + 1):
        lst.append(i)
    print(lst)
    return lst[a - 1] * lst[b - 1]

print(a_and_b(int(input('N: ')), int(input('a: ')), int(input('b: '))))


# Р—Р°РґР°РЅРёРµ 5 Р РµР°Р»РёР·СѓР№С‚Рµ Р°Р»РіРѕСЂРёС‚Рј РїРµСЂРµРјРµС€РёРІР°РЅРёСЏ СЃРїРёСЃРєР°.

import random

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def mix_lst(lst):
    for i in range(len(lst)):
        random_index = random.randint(0, len(lst) - 1)
        temp = lst[i]
        lst[i] = lst[random_index]
        lst[random_index] = temp
    return lst
print(mix_lst(lst))





# 1 Р—Р°РґР°Р№С‚Рµ СЃРїРёСЃРѕРє РёР· РЅРµСЃРєРѕР»СЊРєРёС… С‡РёСЃРµР». РќР°РїРёС€РёС‚Рµ РїСЂРѕРіСЂР°РјРјСѓ,
# РєРѕС‚РѕСЂР°СЏ РЅР°Р№РґС‘С‚ СЃСѓРјРјСѓ СЌР»РµРјРµРЅС‚РѕРІ СЃРїРёСЃРєР°, СЃС‚РѕСЏС‰РёС… РЅР° РЅРµС‡С‘С‚РЅРѕР№ РїРѕР·РёС†РёРё.
# РџСЂРёРјРµСЂ: [2, 3, 5, 9, 3] -> РЅР° РЅРµС‡С‘С‚РЅС‹С… РїРѕР·РёС†РёСЏС… СЌР»РµРјРµРЅС‚С‹ 3 Рё 9, РѕС‚РІРµС‚: 12


lst = [2, 3, 5, 9, 3]

def sum_odd_elem(lst):
    sum = 0
    for i in range(1, len(lst), 2):
        sum += lst[i]
    return sum

print(sum_odd_elem(lst))


# 2 РќР°РїРёС€РёС‚Рµ РїСЂРѕРіСЂР°РјРјСѓ, РєРѕС‚РѕСЂР°СЏ РЅР°Р№РґС‘С‚ РїСЂРѕРёР·РІРµРґРµРЅРёРµ РїР°СЂ С‡РёСЃРµР» СЃРїРёСЃРєР°.
# РџР°СЂРѕР№ СЃС‡РёС‚Р°РµРј РїРµСЂРІС‹Р№ Рё РїРѕСЃР»РµРґРЅРёР№ СЌР»РµРјРµРЅС‚, РІС‚РѕСЂРѕР№ Рё РїСЂРµРґРїРѕСЃР»РµРґРЅРёР№ Рё С‚.Рґ.
# РџСЂРёРјРµСЂ:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


lst1 = [2, 3, 4, 5, 6]
lst2 = [2, 3, 5, 6]

def lst_f_and_l(lst):
    lst_f_and_l = []
    c = len(lst) -1
    for i in range(round((len(lst) + 1) / 2)):
        lst_f_and_l.append(lst[i] * lst[c])
        c -= 1
    return lst_f_and_l

print(lst_f_and_l(lst1))


# 3 Р—Р°РґР°Р№С‚Рµ СЃРїРёСЃРѕРє РёР· РІРµС‰РµСЃС‚РІРµРЅРЅС‹С… С‡РёСЃРµР». РќР°РїРёС€РёС‚Рµ РїСЂРѕРіСЂР°РјРјСѓ,
# РєРѕС‚РѕСЂР°СЏ РЅР°Р№РґС‘С‚ СЂР°Р·РЅРёС†Сѓ РјРµР¶РґСѓ РјР°РєСЃРёРјР°Р»СЊРЅС‹Рј Рё РјРёРЅРёРјР°Р»СЊРЅС‹Рј Р·РЅР°С‡РµРЅРёРµРј РґСЂРѕР±РЅРѕР№ С‡Р°СЃС‚Рё СЌР»РµРјРµРЅС‚РѕРІ.
# РџСЂРёРјРµСЂ:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


lst4 = [1.1, 1.2, 3.1, 5, 10.01]


def difference_max_min(lst):
    min_ = round(lst[0] - int(lst[0]), 2)
    max_ = round(lst[0] - int(lst[0]), 2)
    for i in lst:
        i = round(i - int(i), 2)
        if i != 0:
            if i > max_:
                max_ = i
            if i < min_:
                min_ = i
    return max_ - min_


print(difference_max_min(lst4))


# 4 РќР°РїРёС€РёС‚Рµ РїСЂРѕРіСЂР°РјРјСѓ, РєРѕС‚РѕСЂР°СЏ Р±СѓРґРµС‚ РїСЂРµРѕР±СЂР°Р·РѕРІС‹РІР°С‚СЊ РґРµСЃСЏС‚РёС‡РЅРѕРµ С‡РёСЃР»Рѕ
# РІ РґРІРѕРёС‡РЅРѕРµ.
# РџСЂРёРјРµСЂ:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


num = 45


def change_num(num_):
    lst_ = []

    while int(num_):
        lst_.append(num_ % 2)
        num_ = int(num_ / 2)

    for i in lst_[::-1]:
        print(i, end='')


change_num(num)


# 5 Р—Р°РґР°Р№С‚Рµ С‡РёСЃР»Рѕ. РЎРѕСЃС‚Р°РІСЊС‚Рµ СЃРїРёСЃРѕРє С‡РёСЃРµР» Р¤РёР±РѕРЅР°С‡С‡Рё,
# РІ С‚РѕРј С‡РёСЃР»Рµ РґР»СЏ РѕС‚СЂРёС†Р°С‚РµР»СЊРЅС‹С… РёРЅРґРµРєСЃРѕРІ.
# РџСЂРёРјРµСЂ: РґР»СЏ k = 8 СЃРїРёСЃРѕРє Р±СѓРґРµС‚ РІС‹РіР»СЏРґРµС‚СЊ С‚Р°Рє:
# [-21 ,13, -8, 5, в€’3, 2, в€’1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


n = 8

def fib(num):
    num1 = 1
    num2 = 1
    for i in range(2, num):
        num1, num2 = num2, num1 + num2
    return num2

def neg_fib(num):
    if num == 1:
        return 1
    elif num == 2:
        return -1
    else:
        num1 = 1
        num2 = -1
        for i in range(2, num):
            num1, num2 = num2, num1 - num2
        return num2

lst5 = [0]

for i in range(1, n + 1):
    lst5.append(fib(i))
    lst5.insert(0, neg_fib(i))
print(lst5)





# 1 Р’С‹С‡РёСЃР»РёС‚СЊ С‡РёСЃР»Рѕ ПЂ c Р·Р°РґР°РЅРЅРѕР№ С‚РѕС‡РЅРѕСЃС‚СЊСЋ d
# РџСЂРёРјРµСЂ: РїСЂРё $d = 0.001, ПЂ = 3.141.$    $10^{-1} в‰¤ d в‰¤10^{-10}$2 Р—Р°РґР°Р№С‚Рµ РЅР°С‚СѓСЂР°Р»СЊРЅРѕРµ С‡РёСЃР»Рѕ N. РќР°РїРёС€РёС‚Рµ РїСЂРѕРіСЂР°РјРјСѓ, РєРѕС‚РѕСЂР°СЏ СЃРѕСЃС‚Р°РІРёС‚ СЃРїРёСЃРѕРє РїСЂРѕСЃС‚С‹С… РјРЅРѕР¶РёС‚РµР»РµР№ С‡РёСЃР»Р° N.


num, d = list(map(int, input('Enter num and d separated by a space: ').split()))

def pi_d(num, d):
    pi_ = str(sum(1/16**i*(4/(8*i + 1) - 2/(8*i + 4) - 1/(8*i + 5) - 1/(8*i + 6)) for i in range(num))).split('.')
    str_ = ''
    for i in range(d):
        str_ += str(pi_[1])[i]
    pi_[1] = str_
    return '.'.join(pi_)

print(pi_d(num, d))


# 2 Р—Р°РґР°Р№С‚Рµ РЅР°С‚СѓСЂР°Р»СЊРЅРѕРµ С‡РёСЃР»Рѕ N. РќР°РїРёС€РёС‚Рµ РїСЂРѕРіСЂР°РјРјСѓ, РєРѕС‚РѕСЂР°СЏ СЃРѕСЃС‚Р°РІРёС‚
# СЃРїРёСЃРѕРє РїСЂРѕСЃС‚С‹С… РјРЅРѕР¶РёС‚РµР»РµР№ С‡РёСЃР»Р° N.
# РџСЂРёРјРµСЂ: РїСЂРё N = 236  -> [2, 2, 59]


n = int(input('n: '))

def simple_multipliers(n):
    lst = []
    i = 2
    while i <= n:
        if n % i == 0:
            lst.append(i)
            n /= i
        else:
            i += 1
    return lst

print(simple_multipliers(n))


# 3 Р—Р°РґР°Р№С‚Рµ РїРѕСЃР»РµРґРѕРІР°С‚РµР»СЊРЅРѕСЃС‚СЊ С‡РёСЃРµР». РќР°РїРёС€РёС‚Рµ РїСЂРѕРіСЂР°РјРјСѓ,
# РєРѕС‚РѕСЂР°СЏ РІС‹РІРµРґРµС‚ СЃРїРёСЃРѕРє РЅРµРїРѕРІС‚РѕСЂСЏСЋС‰РёС…СЃСЏ СЌР»РµРјРµРЅС‚РѕРІ РёСЃС…РѕРґРЅРѕР№ РїРѕСЃР»РµРґРѕРІР°С‚РµР»СЊРЅРѕСЃС‚Рё.
# РџСЂРёРјРµСЂ РїСЂРё [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9] -> [2, 4, 5, 9]


lst_ = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]
lst_ = list(set(lst_))
print(lst_)


# 3.2


lst = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]

def non_repeat_elements(lst):
    new_lst = []
    for i in lst:
        if i in new_lst:
            continue
        else:
            new_lst.append(i)
    return  new_lst

print(non_repeat_elements(lst))


# 4) РћРїСЂРµРґРµР»РёС‚СЊ, РїРѕР·РёС†РёСЋ РІС‚РѕСЂРѕРіРѕ РІС…РѕР¶РґРµРЅРёСЏ СЃС‚СЂРѕРєРё РІ СЃРїРёСЃРєРµ Р»РёР±Рѕ СЃРѕРѕР±С‰РёС‚СЊ, С‡С‚Рѕ РµС‘ РЅРµС‚.
# РџСЂРёРјРµСЂС‹
# СЃРїРёСЃРѕРє: ["qwe", "asd", "zxc", "qwe", "ertqwe"], РёС‰РµРј: "qwe", РѕС‚РІРµС‚: 3
# СЃРїРёСЃРѕРє: ["Р№С†Сѓ", "С„С‹РІ", "СЏС‡СЃ", "С†СѓРє", "Р№С†СѓРєРµРЅ", "Р№С†Сѓ"], РёС‰РµРј: "Р№С†Сѓ", РѕС‚РІРµС‚: 5
# СЃРїРёСЃРѕРє: ["Р№С†Сѓ", "С„С‹РІ", "СЏС‡СЃ", "С†СѓРє", "Р№С†СѓРєРµРЅ"], РёС‰РµРј: "Р№С†Сѓ", РѕС‚РІРµС‚: -1
# СЃРїРёСЃРѕРє: ["123", "234", 123, "567"], РёС‰РµРј: "123", РѕС‚РІРµС‚: -1
# СЃРїРёСЃРѕРє: [], РёС‰РµРј: "123", РѕС‚РІРµС‚: -1


lst1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
lst2 = ["Р№С†Сѓ", "С„С‹РІ", "СЏС‡СЃ", "С†СѓРє", "Р№С†СѓРєРµРЅ", "Р№С†Сѓ"]
lst3 = ["Р№С†Сѓ", "С„С‹РІ", "СЏС‡СЃ", "С†СѓРє", "Р№С†СѓРєРµРЅ"]
str1 = "qwe"
str2 = "Р№С†Сѓ"
str3 = "Р№С†Сѓ"

def second(lst, str):
    count = 0
    for i in range(len(lst)):
        if len(lst[i]) > len(str):
            length = len(lst[i]) - len(str)
            for j in range(length):
                if str == lst[j:j + len(str)]:
                    count += 1
        elif lst[i] == str:
            count += 1
            if count == 2:
                print(i)
                break

second(lst1, str1)





# 2. РЎРѕР·РґР°Р№С‚Рµ РїСЂРѕРіСЂР°РјРјСѓ РґР»СЏ РёРіСЂС‹ СЃ РєРѕРЅС„РµС‚Р°РјРё С‡РµР»РѕРІРµРє РїСЂРѕС‚РёРІ С‡РµР»РѕРІРµРєР°.
# РЈСЃР»РѕРІРёРµ Р·Р°РґР°С‡Рё: РќР° СЃС‚РѕР»Рµ Р»РµР¶РёС‚ 2021 РєРѕРЅС„РµС‚Р°.
# РРіСЂР°СЋС‚ РґРІР° РёРіСЂРѕРєР° РґРµР»Р°СЏ С…РѕРґ РґСЂСѓРі РїРѕСЃР»Рµ РґСЂСѓРіР°.
# РџРµСЂРІС‹Р№ С…РѕРґ РѕРїСЂРµРґРµР»СЏРµС‚СЃСЏ Р¶РµСЂРµР±СЊС‘РІРєРѕР№.
# Р—Р° РѕРґРёРЅ С…РѕРґ РјРѕР¶РЅРѕ Р·Р°Р±СЂР°С‚СЊ РЅРµ Р±РѕР»РµРµ С‡РµРј 28 РєРѕРЅС„РµС‚.
# Р’СЃРµ РєРѕРЅС„РµС‚С‹ РѕРїРїРѕРЅРµРЅС‚Р° РґРѕСЃС‚Р°СЋС‚СЃСЏ СЃРґРµР»Р°РІС€РµРјСѓ РїРѕСЃР»РµРґРЅРёР№ С…РѕРґ.
# РЎРєРѕР»СЊРєРѕ РєРѕРЅС„РµС‚ РЅСѓР¶РЅРѕ РІР·СЏС‚СЊ РїРµСЂРІРѕРјСѓ РёРіСЂРѕРєСѓ,
# С‡С‚РѕР±С‹ Р·Р°Р±СЂР°С‚СЊ РІСЃРµ РєРѕРЅС„РµС‚С‹ Сѓ СЃРІРѕРµРіРѕ РєРѕРЅРєСѓСЂРµРЅС‚Р°?
#
# a) Р”РѕР±Р°РІСЊС‚Рµ РёРіСЂСѓ РїСЂРѕС‚РёРІ Р±РѕС‚Р°
# b) РџРѕРґСѓРјР°Р№С‚Рµ РєР°Рє РЅР°РґРµР»РёС‚СЊ Р±РѕС‚Р° ""РёРЅС‚РµР»Р»РµРєС‚РѕРј""


from random import *


print('РЈСЃР»РѕРІРёРµ Р·Р°РґР°С‡Рё: РќР° СЃС‚РѕР»Рµ Р»РµР¶РёС‚ 2021 РєРѕРЅС„РµС‚Р°.\n '
        'РРіСЂР°СЋС‚ РґРІР° РёРіСЂРѕРєР° РґРµР»Р°СЏ С…РѕРґ РґСЂСѓРі РїРѕСЃР»Рµ РґСЂСѓРіР°.\n'
        'РџРµСЂРІС‹Р№ С…РѕРґ РѕРїСЂРµРґРµР»СЏРµС‚СЃСЏ Р¶РµСЂРµР±СЊС‘РІРєРѕР№.\n'
        'Р—Р° РѕРґРёРЅ С…РѕРґ РјРѕР¶РЅРѕ Р·Р°Р±СЂР°С‚СЊ РЅРµ Р±РѕР»РµРµ С‡РµРј 28 РєРѕРЅС„РµС‚.\n'
        'Р’СЃРµ РєРѕРЅС„РµС‚С‹ РѕРїРїРѕРЅРµРЅС‚Р° РґРѕСЃС‚Р°СЋС‚СЃСЏ СЃРґРµР»Р°РІС€РµРјСѓ РїРѕСЃР»РµРґРЅРёР№ С…РѕРґ.\n'
        'РЎРєРѕР»СЊРєРѕ РєРѕРЅС„РµС‚ РЅСѓР¶РЅРѕ РІР·СЏС‚СЊ РїРµСЂРІРѕРјСѓ РёРіСЂРѕРєСѓ,\n'
        'С‡С‚РѕР±С‹ Р·Р°Р±СЂР°С‚СЊ РІСЃРµ РєРѕРЅС„РµС‚С‹ Сѓ СЃРІРѕРµРіРѕ РєРѕРЅРєСѓСЂРµРЅС‚Р°?')


def player_with_player():
    total = 2021
    max_ = 28
    count = 0
    player_1 = input('\nplayer 1: ')
    player_2 = input('\nplayer 2: ')

    print('\nР–РµСЂРµР±СЊС‘РІРєР°: \n')

    x = randint(1, 2)
    if x == 1:
        first = player_1
        second = player_2
    else:
        first = player_2
        second = player_1
    print(f'{first=}')

    while total > 0:
        if count == 0:
            step = int(input(f'\n{first}: '))
            if step > total or step > max_:
                step = int(input(f'\n{max_=} {first}: '))
            total = total - step
        if total > 0:
            print(f'\n{total}')
            count = 1
        else:
            print('Finish')

        if count == 1:
            step = int(input(f'\n{second}: '))
            if step > total or step > max_:
                step = int(input(
                    f'\n{max_=} {second}: '))
            total = total - step
        if total > 0:
            print(f'\n{total}')
            count = 0
        else:
            print('Finish')

    if count == 1:
        print(f'{second} РџРћР‘Р•Р”РР›')
    if count == 0:
        print(f'{first} РџРћР‘Р•Р”РР›')


print('\nplayer with playe '), player_with_player()


def player_with_bot():
    total = 2021
    max_ = 28
    player_1 = input('\nplayer 1: ')
    player_2 = 'РљРѕРјРїСЊСЋС‚РµСЂ'
    players = [player_1, player_2]

    print('\nР–РµСЂРµР±СЊС‘РІРєР°: \n')

    first = randint(-1, 0)

    print(f'{players[first+1]}')

    while total > 0:
        first += 1

        if players[first % 2] == 'РљРѕРјРїСЊСЋС‚РµСЂ':
            print(
                f'\n{players[first%2]} \n{total}: ')

            if total < 29:
                step = total
            else:
                delenie = total//28
                step = total - ((delenie*max_)+1)
                if step == -1:
                    step = max_ -1
                if step == 0:
                    step = max_
            while step > 28 or step < 1:
                step = randint(1,28)
            print(step)
        else:
            step = int(input(f'\n{players[first%2]} \n{total}: '))
            while step > max_ or step > total:
                step = int(input(f'\n{max_}: '))
        total = total - step

    print(f'{total} \nРџРѕР±РµРґРёР» {players[first%2]}')

print('\nplayer with bot'), player_with_bot()
print('\nР§С‚РѕР±С‹ Р·Р°Р±СЂР°С‚СЊ РІСЃРµ РєРѕРЅС„РµС‚С‹ РЅСѓР¶РЅРѕ С‡С‚РѕР±С‹ РІ СЏС‰РёРєРµ РІСЃС‘ РІСЂРµРјСЏ РѕСЃС‚Р°РІР°Р»РѕСЃСЊ РЅРµС‡С‘С‚РЅРѕРµ С‡РёСЃР»Рѕ.\n')


# 1. РќР°РїРёС€РёС‚Рµ РїСЂРѕРіСЂР°РјРјСѓ, СѓРґР°Р»СЏСЋС‰СѓСЋ РёР· С‚РµРєСЃС‚Р° РІСЃРµ СЃР»РѕРІР° СЃРѕРґРµСЂР¶Р°С‰РёРµ "abc".


def write_and_read_file(note_, file_name_):
    with open(file_name_, 'w') as data:
        data.write(note_)
    with open(file_name_, 'r') as data:
        return data.read()


note1 = 'abc fhfg abdj abcdfg'
file_name1 = 'file_hw_5_2_p.txt'
check = 'abc'

res1 = write_and_read_file(note1, file_name1)
print(res1)

res1 = write_and_read_file(' '.join(list(filter(lambda x: x.find(check), res1.split()))), file_name1)
print(res1 + '\n')





#1. Р’С‹ РєРѕРіРґР°-РЅРёР±СѓРґСЊ РёРіСЂР°Р»Рё РІ РёРіСЂСѓ "РљСЂРµСЃС‚РёРєРё-РЅРѕР»РёРєРё"?
# РџРѕРїСЂРѕР±СѓР№С‚Рµ СЃРѕР·РґР°С‚СЊ РµС‘.

from random import *

game = list(range(1, 10))

def start():
    print('РљСЂРµСЃС‚РёРєРё-РЅРѕР»РёРєРё')
    player_1 = input('player 1: ')
    player_2 = input('player 2: ')

    x = randint(1, 2)
    if x == 1:
        first = player_1
    else:
        first = player_2
    print(f'{first=}')


def draw_game(game):
    print('-' * 13)
    for i in range(3):
        print('|', game[0+i*3], '|', game[1+i*3], '|', game[2+i*3], '|')
        print('-' * 13)


def take_input(player_token):
    win = False
    while not win:
        player_answer = input('РљСѓРґР° РїРѕСЃС‚Р°РІРёС‚Рµ ' + player_token + '? ')
        try:
            player_answer = int(player_answer)
        except:
            print('Р’РІРµРґРёС‚Рµ С‡РёСЃР»Рѕ!')
            continue
        if player_answer >= 1 and player_answer <= 9:
            if(str(game[player_answer-1]) not in 'XO'):
                game[player_answer-1] = player_token
                win = True
            else:
                print('Р­С‚Р° РєР»РµС‚РєР° СѓР¶Рµ Р·Р°РЅСЏС‚Р°!')
        else:
            print('Р’РІРµРґРёС‚Рµ С‡РёСЃР»Рѕ РѕС‚ 1 РґРѕ 9!')


def check_win(game):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if game[each[0]] == game[each[1]] == game[each[2]]:
            return game[each[0]]
    return False


def main(game):
    count = 0
    win = False
    while not win:
        draw_game(game)
        if count % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        count += 1
        if count > 4:
            tmp = check_win(game)
            if tmp:
                print(tmp, 'Р’С‹РёРіСЂР°Р»!')
                break
        if count == 9:
            print('РќРёС‡СЊСЏ!')
            break
    draw_game(game)


start()
main(game)
print('\n')


#2 Р—Р°РґР°РЅР° РЅР°С‚СѓСЂР°Р»СЊРЅР°СЏ СЃС‚РµРїРµРЅСЊ k. РЎС„РѕСЂРјРёСЂРѕРІР°С‚СЊ СЃР»СѓС‡Р°Р№РЅС‹Рј РѕР±СЂР°Р·РѕРј СЃРїРёСЃРѕРє РєРѕСЌС„С„РёС†РёРµРЅС‚РѕРІ
# (Р·РЅР°С‡РµРЅРёСЏ РѕС‚ 0 РґРѕ 100) РјРЅРѕРіРѕС‡Р»РµРЅР° Рё Р·Р°РїРёСЃР°С‚СЊ РІ С„Р°Р№Р» РјРЅРѕРіРѕС‡Р»РµРЅ СЃС‚РµРїРµРЅРё k.
# РџСЂРёРјРµСЂ:k=2 => 2*xВІ + 4*x + 5 = 0 РёР»Рё xВІ + 5 = 0 РёР»Рё 10*xВІ = 0


from random import randint

degree = int(input('Degree: '))

def write_file(note, file_name):
    with open(file_name, 'w') as data:
        data.write(note)

def create_list(degree):
    lst = []
    for i in range(degree + 1):
        lst.append(randint(0, 101))
    return lst

def create_note(lst):
    lst_rev = lst[::-1]
    note = ''
    if len(lst_rev) < 1:
        note = 'x = 0'
    else:
        for i in range(len(lst_rev)):
            if i != len(lst_rev) - 1 and lst_rev[i] != 0 and i != len(lst_rev) - 2:
                note += f'{lst_rev[i]}x^{len(lst_rev) - i - 1}'
                if lst_rev[i + 1] != 0:
                    note += ' + '
            elif i == len(lst_rev) - 2 and lst_rev[i] != 0:
                note += f'{lst_rev[i]}x'
                if lst_rev[i + 1] != 0:
                    note += ' + '
            elif i == len(lst_rev) - 1 and lst_rev[i] != 0:
                note += f'{lst_rev[i]} = 0'
            elif i == len(lst_rev) - 1 and lst_rev[i] == 0:
                note += ' = 0'
    return note

coefficient = create_list(degree)
file_name = 'file_hw_4_pr.txt'

write_file(create_note(coefficient), file_name)


#3 Р”Р°РЅС‹ РґРІР° С„Р°Р№Р»Р°, РІ РєР°Р¶РґРѕРј РёР· РєРѕС‚РѕСЂС‹С… РЅР°С…РѕРґРёС‚СЃСЏ Р·Р°РїРёСЃСЊ РјРЅРѕРіРѕС‡Р»РµРЅР°.
# Р—Р°РґР°С‡Р° - СЃС„РѕСЂРјРёСЂРѕРІР°С‚СЊ С„Р°Р№Р», СЃРѕРґРµСЂР¶Р°С‰РёР№ СЃСѓРјРјСѓ РјРЅРѕРіРѕС‡Р»РµРЅРѕРІ.


def read_file(file_name):
    with open(file_name, 'r') as data:
        return data.read()


coefficient1 = create_list(degree)
coefficient2 = create_list(degree)

file_name1 = 'file_hw_4_1_pr.txt'
file_name2 = 'file_hw_4_2_pr.txt'
file_name3 = 'file_hw_4_3_pr.txt'

write_file(create_note(coefficient1), file_name1)
write_file(create_note(coefficient2), file_name2)

print(read_file(file_name1)), print(read_file(file_name2))


def preparing_file(file1):
    # file1 = '99x^3 + 10x^2 - 74x + 12 = 0'
    file1 = file1[0:-4]
    file = ''
    lst = []

    for i in range(len(file1)):
        if file1[i] == '^':
            lst.append(i)
        elif file1[i] == 'x':
            file = file1.replace(file1[i], '')
    for i in range(len(lst)):
        file = file.replace(file1[lst[i]:lst[i] + 2], '')
    return file

def sum_files(file1, file2, degree):
    note = ''
    file1 = file1.replace(' + ', ' ').split(' ')
    file2 = file2.replace(' + ', ' ').split(' ')
    for i in range(degree + 1):
        note += str(int(file1[i]) + int(file2[i])) + ' '
    note = str(note).split(' ')
    file3 = ''
    for i in range(len(note)):
        if i < degree-1:
            file3 += (note[i] + 'x^' + str(degree - i)) + ' + '
        elif i < degree:
            file3 += (note[i] + 'x + ')
        else:
            file3 += note[i]
    file3 += ' = 0'
    return file3

res = write_file(sum_files(preparing_file(read_file(file_name1)), preparing_file(read_file(file_name2)), degree), file_name3)

with open('file_hw_4_3_pr.txt', 'r') as f:
    print(f.read())





