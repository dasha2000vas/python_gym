from random import randint


def get_day_of_delivery(n: int, k: int) -> int:
    """
    Defines day of delivery by day of order (n)
    and days before delivery (k).

    Args:
        n (int): Number of day of week when the order was made.
        k (int): Count of days before delivery.

    Returns:
        int: Number of day of week when delivery is planned.

    """
    if not isinstance(n, int) or not isinstance(k, int):
        raise ValueError("n and k must be integers")
    if not 0 <= n <= 6:
        raise ValueError("n must be between 0 and 6")
    if k < 0:
        raise ValueError("k must be positive")
    if (delivery_day := n + k) in (0,1,2,3,4):
        return n + k
    elif delivery_day in (5,6) or delivery_day % 7 in (5, 6):
        return 0
    else:
        return delivery_day % 7


if __name__ == "__main__":
    n, k = randint(0, 6), randint(1, 20)
    print(f"Day of week: {n} \nDays before delivery: {k}")
    print(f"Day of delivery: {get_day_of_delivery(n, k)}")
