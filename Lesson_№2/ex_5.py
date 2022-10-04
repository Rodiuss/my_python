from random import randint
from re import A

def create_list():
    length = int(input('Введите длину списка: '))
    old_list = []
    for i in range(length):
        old_list.append(i)
    print(f'Как было: {old_list}')
    return old_list

def new_list(old_list):
    for i in range(len(old_list)):
        a = randint(0, len(old_list) - 1)
        b = randint(0, len(old_list) - 1)
        old_list[a], old_list[b] = old_list[b], old_list[a]
    return old_list

def main():
    old_list = create_list()
    print(new_list(old_list))

main()