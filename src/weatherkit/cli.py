import argparse
import os

from weatherkit.client import WeatherClient
from weatherkit.formatting import format_current


def main() -> None:
    parser = argparse.ArgumentParser(prog="weatherkit")
    sub = parser.add_subparsers(dest="command", required=True)
    current = sub.add_parser("current")
    current.add_argument("city")
    current.add_argument("--units", choices=["metric", "imperial"], default="metric")
    args = parser.parse_args()
    client = WeatherClient(api_key=os.environ["WEATHERKIT_API_KEY"])
    print(format_current(client.current(args.city), args.units))
