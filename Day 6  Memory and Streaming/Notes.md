# Day 6 - Memory and Streaming

## Objective
To understand how LangGraph stores conversation state across multiple turns and streams agent execution.

## Concepts Covered
- **MemorySaver:** Stores graph state in memory during program execution.
- **Thread ID:** Identifies a conversation and allows its state to be continued.
- **Streaming:** Uses `stream_mode="values"` to display graph state as execution progresses.
- **Conversation history:** Allows the chatbot to retrieve information from earlier messages in the same thread.

## Project File
- `memory_agent.py` — Implements the chatbot, LangGraph state, memory checkpointing, and streaming tests.

## Tests and Results

### Test 1: Save a Name
**Input:** My name is Mobeen.

**Output:** Hello Mobeen! I will remember your name in this conversation.

**Result:** PASS

### Test 2: Remember Across Turns
**Input:** What is my name?

**Output:** Your name is Mobeen.

**Result:** PASS

### Test 3: Start a New Conversation
**Input:** What is my name? (using a new thread ID)

**Output:** I don't know your name because you haven't told me in this conversation.

**Result:** PASS

### Test 4: Streaming
The program displayed the messages generated during each graph execution using `stream_mode="values"`.

**Result:** PASS

## Screenshot of Output
<img width="1874" height="970" alt="image" src="https://github.com/user-attachments/assets/968aa012-6708-453e-bd05-4d0aff5c430a" />

## Conclusion
The Day 6 tests demonstrated that LangGraph can preserve conversation state across multiple turns when the same thread ID is used. A new thread ID starts a separate conversation. Streaming displayed the graph's state during execution.

## Limitation
This version uses rule-based responses to make the memory tests predictable. It demonstrates LangGraph memory and streaming, but it does not perform LLM-based reasoning or tool calling. `MemorySaver` stores state in RAM, so the memory is temporary.
