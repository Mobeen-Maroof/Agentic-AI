
from typing import Annotated, TypedDict

from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver


# ------------------------------------------
# DEFINE AGENT STATE
# ------------------------------------------

class State(TypedDict):
    messages: Annotated[list, add_messages]


# ------------------------------------------
# CHATBOT NODE
# ------------------------------------------

def chatbot(state: State):
    messages = state["messages"]

    # Find the latest user message
    latest_user_message = next(
        message for message in reversed(messages)
        if isinstance(message, HumanMessage)
    )

    question = latest_user_message.content.lower()

    # Read the conversation history to answer memory questions
    if "what is my name" in question or "what's my name" in question:
        name = None

        for message in messages:
            if isinstance(message, HumanMessage):
                content = message.content.strip()

                if content.lower().startswith("my name is "):
                    name = content[11:].strip().rstrip(".")

        if name:
            answer = f"Your name is {name}."
        else:
            answer = "I don't know your name because you haven't told me in this conversation."

    elif question.startswith("my name is "):
        name = latest_user_message.content.strip()[11:].strip().rstrip(".")
        answer = f"Hello {name}! I will remember your name in this conversation."

    else:
        answer = "I can respond to messages and use the conversation history."

    return {"messages": [AIMessage(content=answer)]}


# ------------------------------------------
# BUILD LANGGRAPH
# ------------------------------------------

builder = StateGraph(State)

builder.add_node("chatbot", chatbot)
builder.add_edge(START, "chatbot")

memory = MemorySaver()
agent = builder.compile(checkpointer=memory)


# ------------------------------------------
# THREAD CONFIGURATION
# ------------------------------------------

config = {
    "configurable": {
        "thread_id": "mobeen-day6-session"
    }
}

new_config = {
    "configurable": {
        "thread_id": "mobeen-new-session"
    }
}


# ------------------------------------------
# MEMORY AND STREAMING TESTS
# ------------------------------------------

if __name__ == "__main__":

    print("DAY 6: MEMORY AND STREAMING")
    print("=" * 40)

    print("\nTURN 1: Tell the agent your name")
    for chunk in agent.stream(
        {"messages": [HumanMessage(content="My name is Mobeen.")]},
        config,
        stream_mode="values"
    ):
        chunk["messages"][-1].pretty_print()

    print("\nTURN 2: Ask the agent to remember your name")
    for chunk in agent.stream(
        {"messages": [HumanMessage(content="What is my name?")]},
        config,
        stream_mode="values"
    ):
        chunk["messages"][-1].pretty_print()

    print("\nTURN 3: Ask using a NEW thread ID")
    for chunk in agent.stream(
        {"messages": [HumanMessage(content="What is my name?")]},
        new_config,
        stream_mode="values"
    ):
        chunk["messages"][-1].pretty_print()

    print("\nDay 6 memory and streaming test finished.")
