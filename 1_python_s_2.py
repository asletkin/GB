# num = float(input('Enter number: '))

# if num - int(num) != 0:
#     print(int((num-int(num)) * 10))
# else:
#     print('Enter float')

# num = input('Enter number: ')
#
# if len(num.split('.')) > 1:
#     print(num.split('.')[1][0])
# else:
#     print('Enter float')
#
# print(0.1+0.1+0.1-0.3)

# 1. Напишите программу, которая принимает на вход
# число N и выдаёт последовательность из N членов.
# *Пример: *
# - Для N = 5: 1, -3, 9, -27, 81

n = int(input('Entar n: '))
r = 1
for i in range(n):
    print(r, end=' ')
    r *= -3