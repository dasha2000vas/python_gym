def count_of_cabins(a, b):
    """
     There is a Ferris wheel with an even number of cabins in the amusement park.
     When cabin №A is at the bottom, cabin №B is at the top (A < B, A and B have the same parity)
       Data: number of cabins - A, B
       Task: find the count of cabins on the Ferris wheel
    """
    if a > b:
        raise ValueError("A должно быть меньше B")
    if not (a % 2 == 0 and b % 2 == 0) and not (a % 2 == 1 and b % 2 == 1):
        raise ValueError("A и B должны быть одинаковой четности")
    return 2 * b - 2 * a


if __name__ == "__main__":
    print("В парке развлечений стоит колесо обозрения с четным числом кабинок. "
          "Когда внизу кабина №A, то наверху - №B (A<B, A и B одинаковой четности)")
    a = int(input("№A = "))
    b = int(input("№B = "))
    print(f"Всего {count_of_cabins(a, b)} кабинок")
