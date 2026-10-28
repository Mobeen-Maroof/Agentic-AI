
from datetime import datetime
from typing import Annotated, TypedDict

from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_ollama import ChatOllama

from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition


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


# Connect the Llama 3.2 model to the tools
llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

llm_with_tools = llm.bind_tools(tools)


# Define the agent state
class State(TypedDict):
    messages: Annotated[list, add_messages]


# Chatbot node
def chatbot(state: State):
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": [response]}


# Build the manual LangGraph agent
builder = StateGraph(State)

builder.add_node("chatbot", chatbot)
builder.add_node("tools", ToolNode(tools))

builder.add_edge(START, "chatbot")
builder.add_conditional_edges("chatbot", tools_condition)
builder.add_edge("tools", "chatbot")

agent = builder.compile()


# Run the agent
if __name__ == "__main__":
    question = input("Ask your ReAct agent: ")

    result = agent.invoke(
        {"messages": [HumanMessage(content=question)]}
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
