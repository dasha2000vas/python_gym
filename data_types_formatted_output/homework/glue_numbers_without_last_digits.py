from random import randint

from pydantic import BaseModel, Field


class ThreeDigitNumbers(BaseModel):
    number1: int = Field(ge=100, le=999, description="First three-digit number.")
    number2: int = Field(ge=100, le=999, description="Second three-digit number.")


def glue_numbers_without_last_digits(values: ThreeDigitNumbers) -> int:
    return values.number1 // 10 * 100 + values.number2 // 10


if __name__ == "__main__":
    number1, number2 = randint(100, 999), randint(100, 999)
    print("number1 =", number1, "\nnumber2 =", number2)
    result = glue_numbers_without_last_digits(ThreeDigitNumbers(number1=number1, number2=number2))
    print("Result:", result)
