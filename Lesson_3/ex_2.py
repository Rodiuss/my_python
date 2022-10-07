from math import ceil
from random import randint

length = int(input('Введите длину списка: '))
my_list = []

for i in range(length):
    my_list.append(randint(1, 10))

print(my_list, end=' --> ')

for i in range(length // 2):
    print(my_list[i] * my_list[length - i - 1], end=', ')

if length % 2 != 0:
    print(my_list[ceil(length / 2 - 1)] * my_list[ceil(length / 2 - 1)])