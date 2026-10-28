# Day 7 — Final LangGraph Agent

**Project:** Agentic AI — Week 1: Foundations & LangGraph  
**Author:** Mobeen Maroof  
**Model:** Ollama — Llama 3.2  
**Framework:** LangGraph

## 1. Project Overview

This project combines the concepts learned during Week 1 to build a tool-using AI agent with LangGraph. It uses a manually constructed graph, two tools, conversation memory, and streaming output.

## 2. Features

- **Manual LangGraph:** Builds the graph using `StateGraph`, nodes, edges, and conditional routing.
- **Safe Calculator:** Performs basic arithmetic using a restricted expression evaluator.
- **Current Time Tool:** Returns the local date and time.
- **Conversation Memory:** Uses `MemorySaver` to retain conversation state across turns with the same thread ID.
- **Streaming:** Uses `stream_mode="updates"` to display graph node updates during execution.
- **Interactive CLI:** Accepts multiple questions until the user enters `exit`.

## 3. Tools

### Calculator
Calculates arithmetic expressions such as `25 * 8` and `12 * 9`. The tool restricts expressions to supported arithmetic operations.

### Current Time
Returns the current local date and time, including the timezone when available.

## 4. How It Works

1. The user enters a question.
2. The chatbot node sends the conversation history and instructions to Llama 3.2.
3. The model may request a tool.
4. The tools node executes the selected tool.
5. The result returns to the chatbot node.
6. The graph continues until the model provides a final response.
7. A checkpointer preserves conversation state for the same thread ID.

## 5. Installation and Setup

Install the required packages in your Python environment:

```bash
pip install langgraph langchain-ollama
```

Install Ollama from [ollama.com](https://ollama.com/) and download the model:

```bash
ollama pull llama3.2
```

## 6. Run the Project

Run the program from the project folder:

```bash
python final_agent.py
```

Enter questions such as:

```text
My name is Mobeen.
Use the calculator to calculate 25 * 8.
What is my name, and what is 12 * 9?
What is the current time?
exit
```

## 7. Test Results

| Test | Expected Result | Status |
|---|---|---|
| Calculator: `25 * 8` | `200` | PASS |
| Calculator: `12 * 9` | `108` | PASS |
| Name memory | Remembers Mobeen in the same thread | PASS |
| Current time | Returns time from the tool | PASS |
| Streaming | Displays graph node updates | PASS |
| Interactive loop | Exits when `exit` is entered | PASS |

**Observation:** The model occasionally selects an unnecessary tool or produces malformed tool-like text. The tested graph still executed the requested calculations and returned the correct results.

### Screenshots of Output
<img width="1910" height="995" alt="image" src="https://github.com/user-attachments/assets/6154906b-d900-4a2e-a67b-fde12d361365" />
<img width="1891" height="1008" alt="image" src="https://github.com/user-attachments/assets/3475793f-3a1c-40f9-9268-c1befcbaddae" />
<img width="1896" height="1012" alt="image" src="https://github.com/user-attachments/assets/312f77d8-2a63-4847-827a-60e1d74a0c4c" />
<img width="1904" height="1009" alt="image" src="https://github.com/user-attachments/assets/60e44237-6e25-4621-8a33-75afbba58c3d" />

## 8. Limitations

- `MemorySaver` stores state in RAM, so memory does not persist after the program stops.
- The model may not always select the most appropriate tool.
- The current-time tool depends on the computer's local clock and timezone.
- This is an educational project, not a production deployment.

## 9. Project Files

```text
Day-7-Final-Agent/
├── final_agent.py
└── README.md
```

## 10. Conclusion

This project demonstrates how LangGraph can combine tools, conditional routing, conversation memory, and streaming in a single agent. It brings together the main implementation concepts practiced during Week 1.

**Future improvement:** Add stronger tool-selection instructions, improve output validation, and explore connecting external tools through the Model Context Protocol (MCP).
