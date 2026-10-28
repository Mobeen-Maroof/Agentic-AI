
from typing import Annotated, TypedDict
from datetime import datetime
import ast
import operator

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.tools import tool
from langchain_ollama import ChatOllama

from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver


# ==========================================
# TOOL 1: SAFE CALCULATOR
# ==========================================

@tool
def calculator(expression: str) -> str:
    """Calculate basic arithmetic, for example 25 * 8 or (12 + 9) / 3."""

    allowed_operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.USub: operator.neg,
        ast.UAdd: operator.pos,
        ast.Pow: operator.pow,
    }

    def evaluate(node):
        if isinstance(node, ast.Expression):
            return evaluate(node.body)

        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return node.value

        if isinstance(node, ast.BinOp) and type(node.op) in allowed_operators:
            left = evaluate(node.left)
            right = evaluate(node.right)

            if isinstance(node.op, ast.Pow) and abs(right) > 10:
                raise ValueError("Exponent is too large.")

            return allowed_operators[type(node.op)](left, right)

        if isinstance(node, ast.UnaryOp) and type(node.op) in allowed_operators:
            return allowed_operators[type(node.op)](evaluate(node.operand))

        raise ValueError("Only basic arithmetic is allowed.")

    try:
        if not expression or len(expression) > 100:
            return "Error: Invalid expression."

        result = evaluate(ast.parse(expression, mode="eval"))

        if isinstance(result, complex) or abs(result) > 1e100:
            return "Error: Result is too large or unsupported."

        return str(result)

    except Exception:
        return "Error: Use a valid basic arithmetic expression."


# ==========================================
# TOOL 2: CURRENT DATE AND TIME
# ==========================================

@tool
def current_time() -> str:
    """Return the current local date and time."""

    return datetime.now().astimezone().strftime(
        "%Y-%m-%d %I:%M:%S %p %Z"
    )


tools = [calculator, current_time]


# ==========================================
# INITIALIZE THE OLLAMA MODEL
# ==========================================

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

llm_with_tools = llm.bind_tools(tools)


# ==========================================
# DEFINE THE GRAPH STATE
# ==========================================

class State(TypedDict):
    messages: Annotated[list, add_messages]


# ==========================================
# CHATBOT NODE
# ==========================================

def chatbot(state: State):
    system_message = SystemMessage(
        content=(
            "You are a helpful assistant. "
            "Use the calculator tool for arithmetic questions. "
            "Use the current_time tool when asked for the current date or time. "
            "Use conversation history to remember information the user shared. "
            "Do not invent calculation results or current times. "
            "If you do not know something, say so."
        )
    )

    response = llm_with_tools.invoke(
        [system_message] + state["messages"]
    )

    return {"messages": [response]}


# ==========================================
# BUILD THE LANGGRAPH MANUALLY
# ==========================================

builder = StateGraph(State)

builder.add_node("chatbot", chatbot)
builder.add_node("tools", ToolNode(tools))

builder.add_edge(START, "chatbot")
builder.add_conditional_edges("chatbot", tools_condition)
builder.add_edge("tools", "chatbot")


# ==========================================
# ADD CONVERSATION MEMORY
# ==========================================

memory = MemorySaver()

agent = builder.compile(checkpointer=memory)

config = {
    "configurable": {
        "thread_id": "day7-mobeen-session"
    }
}


# ==========================================
# STREAMING CHAT LOOP
# ==========================================

def run_agent(user_text: str):
    print("\nYOU:", user_text)
    print("-" * 50)

    for chunk in agent.stream(
        {"messages": [HumanMessage(content=user_text)]},
        config,
        stream_mode="updates"
    ):
        for node_name, update in chunk.items():
            print(f"\n[Node: {node_name}]")

            for message in update.get("messages", []):
                message.pretty_print()


# ==========================================
# MAIN PROGRAM
# ==========================================

if __name__ == "__main__":
    print("=" * 50)
    print("DAY 7: FINAL LANGGRAPH AGENT")
    print("Tools: Calculator and Current Time")
    print("Memory: Enabled")
    print("Streaming: Enabled")
    print("Type 'exit' to stop.")
    print("=" * 50)

    while True:
        try:
            user_input = input("\nAsk me something: ").strip()

            if user_input.lower() in {"exit", "quit"}:
                print("Goodbye!")
                break

            if not user_input:
                print("Please enter a question.")
                continue

            run_agent(user_input)

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

        except Exception as error:
            print(f"\nAn error occurred: {error}")
