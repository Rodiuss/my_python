print("Дано следующее логическое утверждение:\n¬(X + Y + Z) = ¬X * ¬Y * ¬Z")
x = int(input("Введите значение X: "))
y = int(input("Введите значение Y: "))
z = int(input("Введите значение Z: "))

if bool(not(x or y or z)) == bool(not x and not y and not z):
    print("Устверждение истинно!")
else:
    print("Устверждение ложно!")
