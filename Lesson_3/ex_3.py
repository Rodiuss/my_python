from random import random

length = int(input('Введите длину массива: '))
my_list = []

my_list.append(round(random() * 10, 3))
max_ = my_list[0] % 1
min_ = my_list[0] % 1

for i in range(1, length):
    my_list.append(round(random() * 10, 3))

    if my_list[i] % 1 > max_:
        max_ = my_list[i] % 1

    if my_list[i] % 1 < min_:
        min_ = my_list[i] % 1
    
    print(my_list[i], end=', ')

print('\nmax - min =', round(max_, 3) - round(min_, 3))
