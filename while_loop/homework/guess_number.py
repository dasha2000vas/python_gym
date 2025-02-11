from random import randint


def guess_number() -> None:
    """
    Generates number between 1 and 10
    and prompts user to guess it.
    """
    hidden_number = randint(1, 10)
    answer = "y"
    while answer == "y":
        while hidden_number != (entered_number := int(input("Guess number: "))):
            if hidden_number > entered_number:
                print("Hidden number is higher than entered number")
            else:
                print("Hidden number is lower than entered number")
        print(f"Well done! Hidden number is {hidden_number}")
        answer = input("Play again?(y/n) ").lower()

if __name__ == "__main__":
    guess_number()
