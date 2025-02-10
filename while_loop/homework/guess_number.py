from random import randint


def guess_number() -> None:
    """
    Generates number between 1 and 10 and
    prompts the user to guess it.
    """
    hidden_number = randint(1, 10)
    while True:
        while hidden_number != (entered_number := int(input("Guess number: "))):
            if hidden_number > entered_number:
                print("Hidden number is higher than entered number")
            else:
                print("Hidden number is lower than entered number")
        else:
            print(f"Well done! Hidden number is {hidden_number}")
        if (answer := (input("Play again?(y/n) ")).lower()) == "n":
            break
        elif answer == "y":
            continue


if __name__ == "__main__":
    guess_number()
