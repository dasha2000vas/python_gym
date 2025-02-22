from random import uniform


def declension_of_words_rubles_and_pennies(cost_in_rubles: float) -> str:
    """
    Defines declension of words rubles and pennies after number.

    Args:
        cost_in_rubles (float): Entered number in rubles.

    Returns:
        result (str): Declension of words rubles and pennies.
    """
    if not 0 <= cost_in_rubles <= 100:
        raise ValueError("Entered number must be between 0 and 100.")
    if not isinstance(cost_in_rubles, float):
        raise ValueError("Entered number must be float.")
    if len(str(cost_in_rubles).split(".")[1]) > 2:
        raise ValueError("Entered number must have 2 digits after dot.")
    rubles = int(cost_in_rubles)
    result = str(rubles)
    if rubles % 100 in (11, 12, 13, 14):
        result += " рублей "
    elif rubles % 10 == 1:
        result += " рубль "
    elif rubles % 10 in (2, 3, 4):
        result += " рубля "
    else:
        result += " рублей "
    pennies = int(cost_in_rubles * 100 % 100)
    result += str(pennies)
    if pennies % 100 in (11, 12, 13, 14):
        result += " копеек"
    elif pennies % 10 == 1:
        result += " копейка"
    elif pennies % 10 in (2, 3, 4):
        result += " копейки"
    else:
        result += " копеек"
    return result


if __name__ == "__main__":
    cost_in_rubles = round(uniform(0, 100), 2)
    print(declension_of_words_rubles_and_pennies(cost_in_rubles))
