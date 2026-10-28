
from typing import TypedDict, Annotated

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_core.messages import AIMessage, HumanMessage


# Define the graph state
class State(TypedDict):
    messages: Annotated[list, add_messages]
    use_tool: bool


# Chatbot node
def chatbot(state: State):
    # First response: choose a route for this demonstration
    if state["use_tool"]:
        response = AIMessage(
            content="I need to use a tool.",
            tool_calls=[
                {
                    "name": "demo_tool",
                    "args": {},
                    "id": "call_1",
                    "type": "tool_call",
                }
            ],
        )
        return {"messages": [response]}

    return {
        "messages": [
            AIMessage(content="I can answer directly. No tool is needed.")
        ]
    }


# Placeholder tool node
def tools(state: State):
    print("TOOLS NODE EXECUTED")
    return {
        "messages": [
            AIMessage(content="Tool observation: the demo tool has completed.")
        ],
        "use_tool": False,
    }


# Decide the next path
def route(state: State):
    last_message = state["messages"][-1]

    if getattr(last_message, "tool_calls", None):
        return "tools"

    return "end"


# Build the graph
builder = StateGraph(State)

builder.add_node("chatbot", chatbot)
builder.add_node("tools", tools)

builder.add_edge(START, "chatbot")

builder.add_conditional_edges(
    "chatbot",
    route,
    {
        "tools": "tools",
        "end": END,
    },
)

builder.add_edge("tools", "chatbot")

graph = builder.compile()


# Test both routing paths
if __name__ == "__main__":
    print("\nTEST 1: Direct route to END")
    result1 = graph.invoke(
        {
            "messages": [HumanMessage(content="Answer directly")],
            "use_tool": False,
        }
    )
    print("Final answer:", result1["messages"][-1].content)

    print("\nTEST 2: Route through TOOLS")
    result2 = graph.invoke(
        {
            "messages": [HumanMessage(content="Use the demo tool")],
            "use_tool": True,
        }
    )
    print("Final answer:", result2["messages"][-1].content)

    print("\nDay 3 routing tests completed.")
