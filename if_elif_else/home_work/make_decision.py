from random import choice, uniform

weather_list = ["clear", "cloudy", "rainfall", "windy"]


def make_decision(temp_out: float, temp_body: float, weather: str) -> str:
    """
    Decides whether to go outside based on body
    temperature, outdoor temperature and weather.

    Args:
        temp_out (float): Outdoor temperature.
        temp_body (float): Body temperature.
        weather (str): Outdoor weather.

    Returns:
        decision (str): Whether to go outside or not.
    """
    if not weather in weather_list:
        raise ValueError(f"Weather {weather} is not in {weather_list}.")
    if not -30 <= temp_out <= 30:
        raise ValueError("Temperature must be between -30 and 30.")
    if not 35 <= temp_body <= 42:
        raise ValueError("Temperature of body must be between 35 and 42.")
    if (
        35.5 <= temp_body <= 37 and
        -20 <= temp_out <= 20 and
        weather in ["clear", "cloudy"]
    ):
        return "Go outside"
    else:
        return "Stay home"


if __name__ == "__main__":
    # temp_out, temp_body, weather = uniform(-30, 30), uniform(35, 42), choice(weather_list)
    temp_out, temp_body, weather = 0, 100, weather_list[0]
    print(f"temp_body: {temp_body:.1f} \ntemp_out: {temp_out:.1f} \nweather: {weather}")
    print(make_decision(temp_out, temp_body, weather))
