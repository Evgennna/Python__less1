one = 1
two = 2
nine = 9
ten = 10
hungred = 100
thousand = 1000

while True:
    number = int(input("Введите число от 1 до 999: "))

    if one <= number <= nine:
        result = f"Введена цифра. Квадрат числа: {number ** two}"
    elif ten <= number < hungred:
        digit_1 = number // ten
        digit_2 = number % ten
        result = f"Введено двухзначное число. Произведение цифр: {digit_1 * digit_2}"

    elif hungred <= number < thousand:
        result = f"Введено трехзначное число. Зеркальное отображение: {int(str(number)[::-one])}"

    else:
        print("Введено число вне диапазона от 1 до 999. Попробуйте снова.")
        continue

        print(result)
        break


