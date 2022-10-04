number = int(input('Введите число: '))
temp = 1
result = []

for i in range(1, number + 1):
    result.append(temp * i)
    temp = result[i - 1]

print(result)
