# Day 1 — Foundations of Agentic AI

## Part 1: Audit of My Previous AI Capstone

My previous AI capstone was a Secure Research Assistant built using Ollama and the Llama 3.2 model. It included tool calling, reasoning, guardrails, and multiple agents.

### 1. Reflection

**Pattern:** Reflection means reviewing an initial answer, identifying problems, and improving the answer.

**Where I used it:** My previous AI projects included a process in which an agent could review and improve its response.

**Improvement:** I can improve this pattern by adding a clear evaluation step that checks whether the answer is accurate and complete before returning it.

### 2. Tool Use

**Pattern:** Tool use allows an AI model to call external functions when it needs additional capabilities.

**Where I used it:** My projects included tools such as a calculator and research-related tools. The model could select an appropriate tool for a task.

**Improvement:** I can improve tool use by validating inputs, handling errors, and checking tool results before using them in the final answer.

### 3. Planning

**Pattern:** Planning breaks a task into smaller steps and helps an agent decide what to do next.

**Where I used it:** My previous agent projects used reasoning and task decomposition to help complete user requests.

**Improvement:** I can improve planning by defining clear steps, checking progress after each step, and changing the plan when necessary.

### 4. Multi-Agent Collaboration

**Pattern:** Multi-agent collaboration uses multiple agents with different responsibilities to complete a task.

**Where I used it:** My Research Assistant Capstone used a Researcher agent to gather information and a Writer agent to prepare the final response.

**Improvement:** I can improve collaboration by defining each agent's responsibility clearly and checking the research before passing it to the Writer agent.

## Part 2: Workflow vs Agent

### Task 1: Generate a Daily Attendance Report

**Type:** Workflow

**Reason:** The task follows predetermined steps: read attendance data, calculate attendance percentages, and generate a report.

### Task 2: Research an Unknown Technical Problem

**Type:** Agent

**Reason:** The system may need to choose different search queries, investigate new information, and decide what to do based on its findings.

### Task 3: Send a Welcome Email to a New Student

**Type:** Workflow

**Reason:** The process follows fixed steps: obtain the student's details, fill in a prepared email template, and send the email.

## Conclusion

Today I reviewed four important Agentic AI patterns: reflection, tool use, planning, and multi-agent collaboration. I also learned that a workflow follows predefined steps, while an agent can make decisions based on intermediate results.
