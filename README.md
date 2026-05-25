# weatherkit

A small Python library and command-line tool to fetch and format weather data.

## Install

    pip install weatherkit

## Quick start

    from weatherkit import WeatherClient
    client = WeatherClient(api_key="...")
    print(client.current("Madrid"))

## Command line

    weatherkit current Madrid --units metric

See docs/usage.md for every command and docs/configuration.md for settings.
