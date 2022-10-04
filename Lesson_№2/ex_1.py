def num_input():
    while True:
        try:
            num = float(input('Введите число: '))
            return num
        except:
            print('Try harder')

def summ(num):
    num = num * (10 ** len(str(num)))
    match num < 0:
        case True: num = -num
    result = 0

    while num > 0:
        result = result + (num % 10)
        num = num // 10

    print(f'Сумма: {result}')

def main():
    num = num_input()
    summ(num=num)

main()

