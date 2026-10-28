# Day 3 — Nodes in LangGraph

## 1. What Are Nodes?

Nodes are Python functions that perform specific tasks in a LangGraph workflow. Each node receives the current state, processes information, and can return updates to the state.

## 2. Nodes Used in This Project

### Chatbot Node
The `chatbot()` function generates a response. In this demonstration, it either answers directly or creates a simulated tool call.

### Tools Node
The `tools()` function represents a tool execution step. It prints a message and returns a hardcoded observation.

### Conditional Routing Function
The `route()` function checks the latest message. If `tool_calls` exist, it routes to the tools node. Otherwise, it routes to `END`.

## 3. Code Example

```python
def chatbot(state):
    return {
        "messages": [
            AIMessage(content="I can answer directly.")
        ]
    }


def tools(state):
    print("TOOLS NODE EXECUTED")
    return {
        "messages": [
            AIMessage(content="Tool execution completed.")
        ],
        "use_tool": False,
    }


def route(state):
    last_message = state["messages"][-1]

    if getattr(last_message, "tool_calls", None):
        return "tools"

    return "end"
```

## 4. Workflow

**Direct answer:**

`START → chatbot → END`

**Tool execution:**

`START → chatbot → tools → chatbot → END`

## 5. Testing Results

- Test 1: The chatbot answered directly without executing the tools node.
- Test 2: The tools node executed, and the graph returned to the chatbot.
- Both tests completed successfully.

### Screenshot of output
<img width="1899" height="988" alt="image" src="https://github.com/user-attachments/assets/fb4845c2-b7cf-48e6-b107-c5069ef1aa09" />

## 6. Conclusion

Nodes perform tasks in a LangGraph workflow. Conditional routing selects the next step, allowing the graph to finish directly or execute a tool node before continuing.
