n = int(input('Введите число: '))
result = []

for i in range(1, n + 1):
    result.append((1 + 1 / i)**i)

print(round(sum(result), 3))
