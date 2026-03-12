def format_current(data: dict, units: str = "metric") -> str:
    temp = data["temp_c"] if units == "metric" else data["temp_f"]
    symbol = "C" if units == "metric" else "F"
    return f"{data['city']}: {temp:.1f} {symbol}, {data['condition']}"
