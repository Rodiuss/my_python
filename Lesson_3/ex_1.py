from random import randint
length = int(input('Введите длину списка: '))
my_list = []
summ = 0

for i in range(length):
    my_list.append(randint(1, 10))
    if my_list[i] % 2 == 0:
        summ += my_list[i]

print(f'{my_list} --> sum = {summ}')
