# Day 2 — First LangGraph

## Objective
To create and run my first LangGraph workflow using Python, LangGraph, and Ollama.

## What I Learned
LangGraph is a Python framework for building AI applications using nodes, edges, and shared state. It helps organize the workflow of an AI application.

## Technologies Used
- Python
- LangGraph
- Ollama
- Llama 3.2

## Workflow

```text
START → chatbot → END
```

- **START:** Begins the workflow.
- **Chatbot Node:** Receives the user's message, sends it to the Llama 3.2 model through Ollama, and returns the response.
- **END:** Completes the workflow.

## Implementation Steps
1. Created a Python file named `hello_graph.py`.
2. Imported `StateGraph`, `START`, and `END` from LangGraph.
3. Defined the message state using `TypedDict` and `add_messages`.
4. Connected the Llama 3.2 model using `ChatOllama`.
5. Created the chatbot node and connected the workflow.
6. Compiled the graph and invoked it with a user message.
7. Printed the model's response.

## Successful Output

```text
Chatbot response:
LangGraph is an open-source, Python-based, high-performance graph library that allows for efficient and scalable graph processing and analysis.
```
## Screenshot of the Output
<img width="1487" height="897" alt="image" src="https://github.com/user-attachments/assets/08eb9849-0518-43a3-b7e7-221466779bbd" />

## Framework vs. Hand-Coded Agent
A hand-coded agent requires me to manage the workflow logic myself. LangGraph provides a structured way to define state, nodes, and edges, making the workflow easier to organize and extend.

## Conclusion
I successfully ran my first LangGraph workflow using Ollama and Llama 3.2. I learned how to define a state, create a chatbot node, connect the workflow, compile the graph, and obtain a response from the language model.
