
from datetime import datetime
from typing import Annotated, TypedDict

from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_ollama import ChatOllama

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition


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


@tool
def current_time() -> str:
    """Get the current local date and time."""

    return datetime.now().astimezone().strftime(
        "%Y-%m-%d %I:%M:%S %p %Z"
    )


# Register both tools with the model and ToolNode.
tools = [calculator, current_time]

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

llm_with_tools = llm.bind_tools(tools)


class State(TypedDict):
    messages: Annotated[list, add_messages]


def chatbot(state: State):
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": [response]}


builder = StateGraph(State)

builder.add_node("chatbot", chatbot)
builder.add_node("tools", ToolNode(tools))

builder.add_edge(START, "chatbot")
builder.add_conditional_edges("chatbot", tools_condition)
builder.add_edge("tools", "chatbot")

graph = builder.compile()


if __name__ == "__main__":
    question = input("Ask a question: ")

    result = graph.invoke(
        {"messages": [HumanMessage(content=question)]}
    )

    print("\n========== EXECUTION TRACE ==========")

    for message in result["messages"]:
        print("\nMessage type:", type(message).__name__)

        if message.content:
            print("Content:", message.content)

        if getattr(message, "tool_calls", None):
            print("Tool calls:", message.tool_calls)

    print("\n========== FINAL AGENT RESPONSE ==========")
    print(result["messages"][-1].content)

    tool_messages = [
        message
        for message in result["messages"]
        if message.type == "tool"
    ]

    if tool_messages:
        print("\nSUCCESS: A tool was executed.")
    else:
        print("\nWARNING: No tool execution was detected.")
