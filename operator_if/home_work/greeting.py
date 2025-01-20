def greeting(name: str) -> str:
    """
    Greetings user if he enters their name.

    Args:
        name (str): Name of user.

    Returns:
        str: Greeting of user or asking them to log in.
    """
    return f"Welcome, {name}" if name else "Please log in"


if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greeting(name))
