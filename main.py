
from ollama import Client
from tools import get_weather

client = Client(host="http://localhost:11434")

SYSTEM_PROMPT = """
You are a helpful AI assistant with access to tools.

Available tools:

get_weather(location: str)
Description: Get the current weather for a location.

To use a tool, respond with an Action containing JSON:

Action:
{
    "action": "get_weather",
    "action_input": {
        "location": "London"
    }
}

Follow this process:

Question: The user's question.

Action: The tool you want to use, in JSON format.

Observation: The result returned by the tool.

Final Answer: Your final response to the user.

IMPORTANT RULES:
- Use tools when external information is required.
- Never invent an Observation.
- Never invent weather data.
- If you need a tool, output only the Action.
- Wait for the actual Observation before answering.
"""

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

print(response.message.content)

print(response.model_dump())

print("\n--- TOOL TEST ---")
observation = get_weather("London")
print("Observation:", observation)