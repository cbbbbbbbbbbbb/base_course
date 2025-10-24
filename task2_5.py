a = int(input('Введите первое целое число (делимое): '))
b = int(input('Введите второе целое число (делитель): '))

if b == 0:
    print('Ошибка: Нельзя делить на ноль!')
elif a % b == 0:
    chastnoe = a // b
    print(f"{a} делится на {b} без остатка.")
    print(f"Частное: {chastnoe}")
else:
    chastnoe = a // b
    ostatok = a % b
    print(f"{a} не делится нацело на {b}.")
    print(f"Частное: {chastnoe}")
    print(f"Остаток: {ostatok}")