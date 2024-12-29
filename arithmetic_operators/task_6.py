def sum_of_digits(number):
    """
       Data: а three-digit integer
       Task: find the sum of digits of the number using next operations: %, //
    """
    if len(str(number)) != 3:
        raise ValueError("Число должно быть трёхзначным!")
    return number // 100 + number // 10 % 10 + number % 10


if __name__ == "__main__":
    number = int(input("Введите целое трехзначное число: "))
    print("Сумма его цифр:", sum_of_digits(number))
