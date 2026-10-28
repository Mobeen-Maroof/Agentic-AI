# Day 5 — ReAct Agent: Manual Graph vs Prebuilt Agent

**Author:** Mobeen Maroof

## Objective
To build a ReAct agent using a manually constructed LangGraph and compare it with a prebuilt agent. The agent uses Ollama with the Llama 3.2 model and two tools: `calculator` and `current_time`.

## Tools Used
- Python 3.12.4
- Ollama
- Llama 3.2
- LangGraph
- LangChain Core
- `langchain_ollama`

## Project Files
- `react_graph.py` — Manually constructed ReAct agent using `StateGraph`, `ToolNode`, and `tools_condition`.
- `react_prebuilt.py` — Prebuilt ReAct agent using `create_react_agent`.
- `reflection.md` — Comparison and learning reflection.

## Implementation

### 1. Manual ReAct Agent
The manual agent uses a chatbot node to call the LLM, a tool node to execute tools, and conditional routing to determine whether the agent should execute a tool or finish.

### 2. Prebuilt ReAct Agent
The prebuilt agent uses a helper function to create the agent with less code. It uses the same model and tools as the manual implementation.

## Test Results

| Test Case | Result | Status |
|---|---|---|
| Calculator: `25 * 8` | `200` | Passed |
| Current date and time | Actual local date and time returned | Passed |
| Manual agent tool execution | Tool calls and results displayed | Passed |
| Prebuilt agent tool execution | Tool calls and results displayed | Passed |

## Three Things LangGraph Handles
1. **Tool execution:** Executes the selected tool and returns its result.
2. **Conditional routing:** Directs the workflow to a tool or ends the process when appropriate.
3. **State and message management:** Maintains messages and passes tool results back to the model.

The prebuilt agent simplifies the process by handling much of the workflow internally.

## Manual vs Prebuilt Agent

| Manual Graph | Prebuilt Agent |
|---|---|
| Nodes and edges are defined explicitly. | Agent setup requires less code. |
| Provides more direct control over the workflow. | Provides a convenient starting point. |
| Useful for understanding and customizing graph logic. | Useful for building agents quickly. |

## Screenshot of Output
<img width="1895" height="972" alt="image" src="https://github.com/user-attachments/assets/7f8199c4-2cd3-4b60-a64c-65bbe98750f1" />
<img width="1887" height="968" alt="image" src="https://github.com/user-attachments/assets/ec7b1a4b-9437-47ac-80de-363b03433acc" />
<img width="1911" height="1007" alt="image" src="https://github.com/user-attachments/assets/9bd02dd6-4c98-4f2f-86e4-69a69666070d" />
<img width="1899" height="975" alt="image" src="https://github.com/user-attachments/assets/8f82ad94-e377-42bc-8f4e-3b44a2fb7224" />

## Conclusion
Day 5 was completed successfully. Both agents were tested using the calculator and current-time tools. The results demonstrated how a ReAct agent selects tools, executes them, receives their outputs, and generates a final response.

**Note:** The installed LangGraph version displayed a deprecation warning for `create_react_agent`, recommending the newer `create_agent` API from `langchain.agents`. The prebuilt implementation nevertheless passed both tests.

