
from datetime import datetime

from langchain_core.tools import tool


@tool
def calculator(expression: str) -> str:
    """Calculate a basic arithmetic expression."""

    allowed_chars = set("0123456789+-*/(). ")

    if not expression or not set(expression) <= allowed_chars:
        return "Error: Invalid arithmetic expression."

    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception:
        return "Error: Could not calculate this expression."


@tool
def current_time() -> str:
    """Get the current local date and time."""

    return datetime.now().astimezone().strftime("%Y-%m-%d %I:%M:%S %p %Z")


if __name__ == "__main__":
    print("Available tools:")

    for available_tool in [calculator, current_time]:
        print("-", available_tool.name, ":", available_tool.description)

    print("\nCalculator test:", calculator.invoke({"expression": "25 * 8"}))
    print("Time test:", current_time.invoke({}))
