
from datetime import datetime

from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent


# Tool 1: Calculator
@tool
def calculator(expression: str) -> str:
    """Calculate a basic arithmetic expression such as 25 * 8."""

    allowed_chars = set("0123456789+-*/(). ")

    if not expression or not set(expression) <= allowed_chars:
        return "Error: Invalid arithmetic expression."

    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception:
        return "Error: Could not calculate this expression."


# Tool 2: Current local date and time
@tool
def current_time() -> str:
    """Get the current local date and time."""

    return datetime.now().astimezone().strftime(
        "%Y-%m-%d %I:%M:%S %p %Z"
    )


# Register tools
tools = [calculator, current_time]


# Initialize the model
llm = ChatOllama(
    model="llama3.2",
    temperature=0
)


# Create the prebuilt ReAct agent
agent = create_react_agent(
    model=llm,
    tools=tools
)


# Run the agent
if __name__ == "__main__":
    question = input("Ask your prebuilt ReAct agent: ")

    result = agent.invoke(
        {"messages": [("user", question)]}
    )

    print("\n========== EXECUTION TRACE ==========")

    for message in result["messages"]:
        print("\nMessage type:", type(message).__name__)

        if message.content:
            print("Content:", message.content)

        if getattr(message, "tool_calls", None):
            print("Tool calls:", message.tool_calls)

    print("\n========== FINAL ANSWER ==========")
    print(result["messages"][-1].content)

    executed_tools = [
        message
        for message in result["messages"]
        if message.type == "tool"
    ]

    print("\nTools executed:", len(executed_tools))
