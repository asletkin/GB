# 1 Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
n = int(input('n: '))

if 0 < n < 6:
    print('No')
elif 5 < n < 8:
    print('Yes')
else:
    print('Mistake')


# 2 Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))
if x > 0 and y > 0 and z > 0 or x < 0 and y < 0 and z < 0:
    print(True)
else:
    print(False)


# 3 Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка.
x = int(input('x: '))
y = int(input('y: '))

if x != 0 and y !=0:
    if x > 0 and y > 0:
        print(1)
    elif x < 0 and y > 0:
        print(2)
    elif x < 0 and y < 0:
        print(3)
    else:
        print(4)
else:
    print('Mistake')


# 4 Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
n = int(input('n: '))

if 0 < n < 5:
    if n == 1:
        print('x > 0 and y > 0')
    elif n == 2:
        print('x < 0 and y > 0')
    elif n == 3:
        print('x < 0 and y < 0')
    else:
        print('x > 0 and y < 0')
else:
    print('Mistake')


# 5 Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
a_x = int(input('a_x: '))
a_y = int(input('a_y: '))
b_x = int(input('b_x: '))
b_y = int(input('b_y: '))

print(((b_x - a_x) ** 2 + (b_y - a_y) ** 2) ** 0.5)