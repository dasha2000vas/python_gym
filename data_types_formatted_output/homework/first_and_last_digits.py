from random import randint

from pydantic import BaseModel, Field


class ThreeDigitNumber(BaseModel):
    number: int = Field(
        ge=100,
        le=999,
        description="Three-digit number."
    )


def swap_first_and_last_digits(value: ThreeDigitNumber) -> int:
    return value.number % 10 * 100 + value.number // 10 % 10 * 10 + value.number // 100


if __name__ == "__main__":
    number = randint(100, 999)
    print("Number:", number)
    print("Result:", swap_first_and_last_digits(ThreeDigitNumber(number=number)))
