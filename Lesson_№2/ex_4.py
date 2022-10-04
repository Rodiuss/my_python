n = int(input('Введите значение N: '))
a = int(input('Ведите значение a: '))
b = int(input('Ведите значение b: '))
array = []
n = abs(n)
for i in range(-n, n + 1):
    array.append(i)

try:
    print(f'{array[a]} * {array[b]} = {array[a] * array[b]}')
except:
    print('Try harder')
