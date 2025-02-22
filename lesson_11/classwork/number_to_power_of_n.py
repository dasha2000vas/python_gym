from random import randint, uniform, choice


def raise_number_to_power_of_n(number: int | float, power: int) -> int | float:
    """
    Raises number to power of n using recursion.

    Args:
        number (int | float): Number to raise.
        power (int): Integer power (>0).

    Returns:
        int | float: Resulting number.
    """
    if not isinstance(number, (int, float)):
        raise ValueError("Number must be integer or float")
    if not isinstance(power, int):
        raise ValueError("Power must be integer")
    if power < 0:
        raise ValueError("Power must be positive")
    if power == 0: return 1
    return number * raise_number_to_power_of_n(number, power - 1)


if __name__ == '__main__':
    number, power = choice([randint(1, 10), uniform(1, 10)]), randint(1, 10)
    print(f"Number: {number:.3f}, power: {power}")
    print(f"Result: {raise_number_to_power_of_n(number, power):.3f}")
