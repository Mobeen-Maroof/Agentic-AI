# Agentic AI — Week 1: Foundations & LangGraph

**Author:** Mobeen Maroof  
**Week:** 1  Foundations & LangGraph  
**Model:** Llama 3.2  
**Framework:** LangGraph  
**Runtime:** Ollama  
**Language:** Python

## Overview

This repository contains my Week 1 work on Agentic AI. During this week, I learned the fundamentals of AI agents, explored agentic design patterns, created LangGraph workflows, connected tools to an agent, implemented a ReAct agent, and experimented with memory and streaming.

The final project combines these concepts into a LangGraph agent that uses a calculator and a current-time tool, maintains conversation history during a session, and streams graph execution updates.

## Learning Objectives

- Understand the difference between an AI agent and a fixed workflow.
- Learn the four agentic design patterns.
- Understand LangGraph's state, nodes, and edges.
- Implement conditional routing.
- Connect Python functions as tools.
- Build and compare ReAct agents.
- Add short-term conversation memory.
- Stream graph execution updates.
- Understand the purpose of Model Context Protocol (MCP).

## Day-by-Day Progress

### Day 1 — Foundations of Agentic AI

**Topics:** AI agents, agentic design patterns, and workflows versus agents.

I learned that an AI agent can decide what action to take, use tools, observe results, and continue working toward a goal.

I studied four agentic design patterns:

1. **Reflection:** Reviewing and improving an output.
2. **Tool Use:** Calling tools to perform tasks or retrieve information.
3. **Planning:** Breaking a goal into smaller steps.
4. **Multi-Agent:** Using multiple specialized agents that collaborate.

I also learned that a fixed workflow is preferable when the steps are already known, while an agent is useful when the next step depends on intermediate results.

**Outcome:** Understood the basic concepts of agentic systems and when to use an agent instead of a fixed workflow.

### Day 2 — Frameworks and the LangGraph Mental Model

**Topics:** LangGraph, state, nodes, and edges.

I learned why frameworks are useful when building agents. Managing tool calls, conversation history, branching, and execution loops manually can become difficult as an application grows.

The three core graph concepts are:

- **State:** Stores information that moves through the graph.
- **Nodes:** Perform operations, such as calling a model or executing a tool.
- **Edges:** Define the path between nodes.

**Outcome:** Learned how to think about an agent as a graph of connected steps and explored the foundation for building agents with LangGraph.

### Day 3 — Conditional Routing

**Topics:** StateGraph, conditional edges, and graph execution.

I created a small LangGraph demonstration to understand how a graph can follow different paths depending on its state or routing decision.

Conditional routing allows an agent to choose the next node instead of always following one fixed sequence.

**Outcome:** Built and tested a conditional-routing graph and learned how branching logic works in LangGraph.

**Project folder:** `Day-3-Conditional-Routing/`

### Day 4 — Real Tools

**Topics:** Python tools, `@tool`, `ToolNode`, and tool routing.

I created an agent that can call real Python functions instead of answering every question directly.

The tools included:

- **Calculator:** Performs arithmetic calculations.
- **Current Time:** Returns the current local date and time.

I used LangGraph's tool execution and routing components to handle tool calls and return their results to the agent.

**Outcome:** Tested tool execution and learned how an agent can use external functions to complete tasks.

**Project folder:** `Day-4-Real-Tools/`

### Day 5 — ReAct Agent

**Topics:** Reasoning and Acting (ReAct), tool selection, and agent loops.

I built a ReAct agent and explored both a manually constructed graph and a prebuilt agent approach.

The ReAct pattern lets an agent choose an action, receive an observation, and continue until it can provide a response.

I tested tool-based questions and compared the manual graph approach with a prebuilt agent implementation.

**Outcome:** Learned how the agent loop works and how LangGraph can organize tool execution and routing.

**Project folder:** `Day-5-ReAct-Agent/`

### Day 6 — Memory and Streaming

**Topics:** Checkpointers, `MemorySaver`, thread IDs, and streaming.

I implemented a memory demonstration using LangGraph's `MemorySaver` checkpointer.

The program used a consistent `thread_id` to retain conversation state across multiple turns. I tested whether the program could remember a name shared earlier in the same conversation and confirmed that a new thread did not automatically share that conversation history.

I also used `stream_mode="values"` to inspect the state as the conversation progressed.

**Outcome:** Demonstrated short-term, in-memory conversation persistence across turns.

**Important limitation:** This Day 6 demonstration used rule-based responses rather than an LLM. Its memory is stored in memory while the program runs and is not durable across restarts.

**Project folder:** `Day-6-Memory-Streaming/`

### Day 7 — Final LangGraph Agent and MCP

**Topics:** Manual LangGraph construction, safe tool execution, memory, and streaming updates.

I combined the week's main concepts into a final interactive agent using Python, LangGraph, Ollama, and Llama 3.2.

The final agent includes:

- **Manual graph construction:** Uses `StateGraph`, nodes, and edges.
- **Calculator tool:** Safely evaluates supported basic arithmetic expressions without unrestricted Python `eval`.
- **Current-time tool:** Returns the current local date and time.
- **Tool execution:** Uses `ToolNode` and `tools_condition` to route tool calls.
- **Conversation memory:** Uses `MemorySaver` and a configured thread ID.
- **Streaming updates:** Uses `agent.stream()` with `stream_mode="updates"` to display graph node updates.
- **Interactive CLI:** Accepts questions until the user enters `exit` or `quit`.

I tested the final agent with questions about a name shared earlier in the conversation, arithmetic calculations, and the current time.

I also studied **Model Context Protocol (MCP)**. MCP provides a standard way for AI applications to connect to tools and data sources exposed by separate MCP servers. This makes tools easier to reuse across compatible applications.

**Outcome:** Built and tested a multi-turn LangGraph agent with two tools, in-memory conversation state, and streamed graph execution updates.

**Project folder:** `Day-7-Final-Agent/`

**Note:** The final project displays graph execution updates; it does not stream every generated text token individually. MCP was studied conceptually and was not connected as a live server in this project.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Ollama | Runs the local language model |
| Llama 3.2 | Language model used by the final agent |
| LangGraph | Builds and controls the agent graph |
| LangChain Core | Provides message and tool abstractions |
| `MemorySaver` | Stores conversation state during the running session |
| PowerShell | Runs commands and tests on Windows |
| Git and GitHub | Version control and project sharing |

## Installation and Setup

### 1. Install Python

Install a compatible Python version and make sure Python is available in PowerShell.

### 2. Install Ollama

Install Ollama from the official website:

https://ollama.com/

### 3. Download the Model

Run the following command in PowerShell:

```powershell
ollama pull llama3.2
```

### 4. Install Python Packages

Activate your virtual environment, then run:

```powershell
pip install langgraph langchain-core langchain-ollama
```

### 5. Run the Final Agent

Navigate to the Day 7 project folder and execute:

```powershell
python final_agent.py
```

Ask questions such as:

```text
My name is Mobeen.
Use the calculator to calculate 25 * 8.
What is my name, and what is 12 * 9?
What is the current time?
exit
```

The agent should demonstrate conversation context, calculator tool execution, current-time retrieval, and graph execution updates. Exact responses may vary because tool selection and natural-language responses are generated by the model.

## Key Learnings

By completing Week 1, I learned:

- How an AI agent differs from a basic language-model call.
- When to choose a fixed workflow instead of a dynamic agent.
- How state, nodes, and edges form a LangGraph.
- How to implement conditional routing and tool execution.
- How to build and compare manual and prebuilt ReAct agents.
- How to use a checkpointer for short-term conversation memory.
- How to stream graph execution updates.
- Why safe tool implementation matters.
- What MCP is and how it supports reusable tool integrations.

## Limitations and Future Improvements

- The final agent's tool selection can occasionally be unnecessary or incorrect.
- `MemorySaver` keeps state in memory and does not provide durable storage after the process ends.
- The current-time tool uses the computer's local time configuration.
- The current streaming implementation displays graph updates rather than token-by-token output.
- MCP was explored conceptually; a live MCP server integration remains future work.
- Future improvements could include stronger tool-call validation, error handling, persistent storage, and additional tools.

## Conclusion

Week 1 helped me move from understanding basic AI-agent loops to organizing an agent as a stateful graph with LangGraph. I practiced conditional routing, tool execution, ReAct, short-term memory, and streaming graph updates.

The final project brings these concepts together in a local Llama 3.2 agent using Ollama. It provides a foundation for further work on long-term memory, planning, agentic retrieval, and more advanced multi-agent systems.
