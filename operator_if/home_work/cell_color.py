from random import randint


def get_cell_color(x: int, y: int) -> str:
    """
    Defines cell color of chessboard
    by row and column numbers.

    Args:
       x (int): Column number.
       y (int): Row number.

    Returns:
       color (str): Cell color.
    """
    if x % 2 and y % 2 or not x % 2 and not y % 2:
        color = "black"
    else:
        color = "white"
    return color


if __name__ == "__main__":
    x, y = randint(1, 8), randint(1, 8)
    print(f"Cell with {x, y} is {get_cell_color(x, y)}")
