# Dummy Agent Library

A lightweight educational project exploring how AI agents work under the hood, using **Python, Ollama, and Qwen3**.

Inspired by the [Hugging Face Agents Course](https://huggingface.co/learn/agents-course/unit1/dummy-agent-library), this project aims to build a simple AI agent from scratch, progressively introducing system prompts, tool definitions, action parsing, tool execution, and agent loops.

The goal is to understand the fundamental mechanics of AI agents before relying on higher-level frameworks.

## Project Status

**Version: 0.1.0 — Prompt-Based Tool Selection**

This initial version demonstrates how a Large Language Model (LLM) can interpret a system prompt, identify an appropriate tool, and generate a structured action.

Currently implemented:

- Local LLM inference using Ollama
- Qwen3 4B integration
- Custom system prompt
- Tool descriptions within the prompt
- Structured JSON action generation through prompting
- Configurable inference parameters
- Response metadata inspection

Not yet implemented:

- Actual tool execution
- JSON action parsing
- Observation handling
- Agent execution loop
- Multiple tools
- Conversation history management

## Architecture

The current execution flow is:

```text
User Question
     |
     v
System Prompt + Messages
     |
     v
Ollama (Qwen3 4B)
     |
     v
LLM Response
     |
     v
Action Description (JSON)
     |
     v
Console Output
```

**Important:** The model currently generates a textual representation of a tool call. No Python function is executed.

This is a prompt-based approach rather than native function calling.

## Technologies

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Ollama | Local model inference |
| Qwen3 4B | Large Language Model |
| Ollama Python SDK | Communication with the local inference server |

All inference runs locally, without requiring external API credentials or paid inference credits.

## Installation

### Prerequisites

- Python 3.13 (recommended for this project)
- [Ollama](https://ollama.com/download)
- Git (optional)

### 1. Download the model

```bash
ollama pull qwen3:4b
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

On Linux or macOS:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install ollama
```

### 4. Run the application

Ensure Ollama is running, then execute:

```bash
python main.py
```

The application connects to the local Ollama server at:

```text
http://localhost:11434
```

## How It Works

### 1. System Prompt

The system prompt defines the assistant's behavior and describes the available tools.

The current tool specification is:

```python
get_weather(location: str)
```

The model receives instructions to use this tool when weather information is requested.

However, the function is not yet implemented in Python.

### 2. Message Structure

The conversation is represented as a list of messages:

```python
messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    },
    {
        "role": "user",
        "content": "What's the weather in London?"
    }
]
```

Each message contains:

- `role`: Identifies the message source.
- `content`: Contains the message text.

The system message provides instructions, while the user message contains the actual request.

### 3. Model Inference

The application communicates with Ollama using:

```python
response = client.chat(
    model="qwen3:4b",
    messages=messages,
    stream=False,
    think=False,
    options={
        "temperature": 0.2,
        "num_predict": 300
    }
)
```

Configuration:

| Parameter | Description |
|---|---|
| `model` | Selects Qwen3 4B |
| `messages` | Provides the conversation context |
| `stream=False` | Returns the completed response |
| `think=False` | Requests disabling extended thinking mode |
| `temperature=0.2` | Reduces generation randomness |
| `num_predict=300` | Limits generated tokens |

### 4. Action Generation

When asked:

```text
What's the weather in London?
```

The model is expected to generate an action similar to:

```json
{
    "action": "get_weather",
    "action_input": {
        "location": "London"
    }
}
```

This demonstrates that the model can select a tool based on instructions provided in natural language.

The generated output is not guaranteed to contain valid JSON exclusively. Additional text may appear, so future versions will require proper parsing and validation.

### 5. Response Inspection

The application prints both the generated content and the full response metadata:

```python
print(response.message.content)

print(response.model_dump())
```

The response metadata can include:

- Model identification
- Generated content
- Token usage
- Inference duration
- Model loading duration
- Completion status

These details are useful for understanding model performance and debugging inference behavior.

## Current Limitations

This version is an educational proof of concept, not a fully functional AI agent.

**Tool calls are not executed.** The model only generates textual instructions describing which tool should be called.

**No observation feedback exists.** The application cannot provide actual tool results back to the model.

**No agent loop exists.** Each execution consists of a single inference request.

**Output formatting is not guaranteed.** The model may include explanatory text alongside the JSON action.

**No real-time weather information is available.** The `get_weather` function is only described in the prompt.

## Roadmap

- [x] Set up local inference with Ollama
- [x] Configure Qwen3 4B
- [x] Create a custom system prompt
- [x] Define a tool interface
- [x] Generate structured actions through prompting
- [x] Inspect model response metadata
- [ ] Implement a Python tool function
- [ ] Parse and validate generated actions
- [ ] Execute tools dynamically
- [ ] Return observations to the model
- [ ] Implement the agent execution loop
- [ ] Support multiple tools
- [ ] Add error handling and automated tests
- [ ] Explore native function calling

## Learning Objectives

This project focuses on understanding:

1. How system prompts influence LLM behavior.
2. How chat messages and roles are structured.
3. How language models select tools.
4. The difference between generating a tool call and executing it.
5. How observations can be incorporated into subsequent model requests.
6. How an iterative execution loop transforms a basic LLM application into an agent.

## References

- [Hugging Face Agents Course](https://huggingface.co/learn/agents-course/)
- [Dummy Agent Library Tutorial](https://huggingface.co/learn/agents-course/unit1/dummy-agent-library)
- [Ollama Documentation](https://docs.ollama.com/)
- [Ollama Python SDK](https://github.com/ollama/ollama-python)
- [Qwen3 on Ollama](https://ollama.com/library/qwen3)

## License

No license has been specified yet.

---

**Project Stage:** 0.1.0

**Focus:** Understanding prompt-based tool selection before implementing real tool execution and agent loops.
