# 1
n = int(input('n: '))

if 0 < n < 6:
    print('No')
elif 5 < n < 8:
    print('Yes')
else:
    print('Mistake')

# 2

x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))
if x > 0 and y > 0 and z > 0 or x < 0 and y < 0 and z < 0:
    print (True)
else:
    print (False)

# 3
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

# 4

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

# 5

a_x = int(input('a_x: '))
a_y = int(input('a_y: '))
b_x = int(input('b_x: '))
b_y = int(input('b_y: '))

print(((b_x - a_x) ** 2 + (b_y - a_y) ** 2) ** (0.5))