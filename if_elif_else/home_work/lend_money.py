from random import choice


def lend_money(
        you_have_money: bool,
        is_drinker: bool,
        returned_earlier: bool,
        is_miser: bool
) -> bool:
    """
    Decides whether to lend money to neighbor
    based on following criteria: have you money,
    is he drinker, did he return debts earlier,
    are you miser.

    Args:
        you_have_money (bool): True if you have money, else False.
        is_drinker (bool): True if neighbor is drinker, else False.
        returned_earlier (bool): True if neighbor returned debts earlier, else False.
        is_miser (bool): True if you are miser, else False.

    Returns:
        bool: True if decision is lend money, else False.
    """
    for criterion in (you_have_money, is_drinker, returned_earlier, is_miser):
        if not isinstance(criterion, bool):
            raise ValueError(f"All criteria must be bool, not {type(criterion)}")
    if you_have_money and not is_drinker and returned_earlier and not is_miser:
        return True
    return False


if __name__ == "__main__":
    choices = [True, False]
    you_have_money, is_drinker, returned_earlier, is_miser = (
        choice(choices), choice(choices), choice(choices), choice(choices)
    )
    print(
        f"You have money: {you_have_money} "
        f"\nNeighbor is drinker: {is_drinker} "
        f"\nReturned earlier: {returned_earlier} "
        f"\nYou are miser: {is_miser}"
    )
    result = lend_money(you_have_money, is_drinker, returned_earlier, is_miser)
    print(f"Will you lend to him? {"Yes" if result else "No"}")
