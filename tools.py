
def get_weather(location: str) -> str:
    """
    Simulate a weather API response.

    Args:
        location: City to retrieve weather for.

    Returns:
        Simulated weather information.
    """
    weather_data = {
        "London": "Cloudy, 15°C",
        "Paris": "Sunny, 22°C",
        "Tokyo": "Rainy, 18°C",
        "Blumenau": "Partly cloudy, 26°C"
    }

    return weather_data.get(
        location,
        f"Weather data unavailable for {location}"
    )


if __name__ == "__main__":
    print(get_weather("London"))
    print(get_weather("Blumenau"))
    print(get_weather("New York"))