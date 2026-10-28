# Day 4 — Real Tools with LangGraph

## 1. Objective
The objective of Day 4 was to create real Python tools and connect them to a LangGraph agent so the AI model can select and execute tools when needed.

## 2. What I Learned
- How to create tools using the `@tool` decorator.
- How to connect tools to an Ollama language model using `bind_tools()`.
- How to create a LangGraph workflow using nodes and edges.
- How to use `ToolNode` to execute tools.
- How to use `tools_condition` for conditional routing.
- How tool results return to the chatbot to generate a final response.

## 3. Tools Implemented

### Calculator
The calculator performs basic arithmetic operations.

Example:
- Input: `25 * 8`
- Output: `200`

### Current Time
The current-time tool returns the local date and time.

Example output:
`2026-10-28 06:21:49 PM Pakistan Standard Time`

## 4. Technologies Used
- Python
- Ollama
- Llama 3.2
- LangChain
- LangGraph

## 5. Project Files
- `tools_agent.py` — Defines and tests the calculator and current-time tools.
- `real_tools_graph.py` — Connects both tools to the LangGraph workflow.
- `notes.md` — Documents the concepts learned and test results.

## 6. How the Workflow Works
1. The user enters a question.
2. The chatbot sends the question to the Llama 3.2 model.
3. The model decides whether a tool is needed.
4. `tools_condition` checks whether the model requested a tool.
5. `ToolNode` executes the requested tool.
6. The tool result is returned to the chatbot.
7. The chatbot generates the final response.

## 7. Testing and Results

### Test 1: Calculator
Question: Use the calculator tool to calculate `25 * 8`.

Result: `200`

Status: Passed.

### Test 2: Current Time
Question: Use the current_time tool to return the current local date and time.

Result: The tool returned the local date and time successfully.

Status: Passed.

### Execution Verification
The execution trace showed:
- `AIMessage` containing the requested tool call.
- `ToolMessage` containing the tool result.
- A final `AIMessage` containing the chatbot's response.

Both tools were successfully called and executed through LangGraph.

## Screenshots of Outputs
<img width="1887" height="888" alt="image" src="https://github.com/user-attachments/assets/75b38235-3081-495e-bd4e-1c2998bbff18" />
<img width="1881" height="988" alt="image" src="https://github.com/user-attachments/assets/4fc9b5fa-4217-463c-a0e2-2f383415a0de" />
<img width="1896" height="969" alt="image" src="https://github.com/user-attachments/assets/6aba5b30-1940-4cca-bc02-d3d230207217" />
<img width="1893" height="974" alt="image" src="https://github.com/user-attachments/assets/f36f82ec-eb18-464c-82b3-e8a2ebce2ad3" />
<img width="1867" height="974" alt="image" src="https://github.com/user-attachments/assets/f7bc573a-ee1a-493c-9388-15e573c8c55a" />
<img width="1855" height="925" alt="image" src="https://github.com/user-attachments/assets/52e09df6-2c62-498e-bef1-16e99ab2b00c" />

## 8. Conclusion
I successfully built and tested a LangGraph agent with two real Python tools: a calculator and a current-time tool. The AI model selected the appropriate tool, LangGraph executed it, and the result returned to the chatbot.


