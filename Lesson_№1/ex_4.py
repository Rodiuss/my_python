num = int(input("Введите номер четверти: "))

match num:
    case 1:
        print("Диапазон: x > 0; y > 0")
    case 2:
        print("Диапазон: x < 0; y > 0")
    case 3:
        print("Диапазон: x < 0; y < 0")
    case 4:
        print("Диапазон: x > 0; y < 0")
    case _:
        print("Try harder")