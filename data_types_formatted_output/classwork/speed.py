from random import randint

from pydantic import BaseModel, Field


class ValuesForFindingSpeed(BaseModel):
    time: int = Field(gt=0, description="Time in hours.")
    distance: int = Field(gt=0, description="Distance in km.")


def get_speed_in_ms(values: ValuesForFindingSpeed) -> float:
    return (values.distance * 1000) / (values.time * 60 * 60)


if __name__ == "__main__":
    time, distance = randint(1, 10), randint(1, 1000)
    print(f"Time: {time} \nDistance: {distance}")
    speed = get_speed_in_ms(
        ValuesForFindingSpeed(time=time, distance=distance)
    )
    print("Answer: with time = %d h and distance = %d km, speed is %.3f m/s" % (time, distance, speed))
