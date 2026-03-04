import httpx

from weatherkit.errors import WeatherAPIError

BASE_URL = "https://api.example-weather.test/v1"


class WeatherClient:
    def __init__(self, api_key: str, timeout: float = 10.0):
        self.api_key = api_key
        self.timeout = timeout

    def current(self, city: str) -> dict:
        response = httpx.get(f"{BASE_URL}/current", params={"q": city, "key": self.api_key}, timeout=self.timeout)
        if response.status_code != 200:
            raise WeatherAPIError(response.status_code, response.text)
        return response.json()
