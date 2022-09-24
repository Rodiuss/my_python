day = int(input("Введите номер дня недели: "))
if day == 6 or day == 7:
    print("Сегодня выходной!")
elif 0 < day < 6:
    print("Сегодня будни!")
else:
    print("Try harder!")
