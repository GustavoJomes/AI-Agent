
import json

from tools import get_weather


# Only registered tools can be executed.
TOOL_REGISTRY = {
    "get_weather": get_weather
}


def parse_action(response_text: str) -> dict:
    """
    Extract and parse the JSON action from an LLM response.
    """
    decoder = json.JSONDecoder()

    # Search for a valid JSON object in the response.
    for index, char in enumerate(response_text):
        if char != "{":
            continue

        try:
            action, _ = decoder.raw_decode(response_text[index:])
        except json.JSONDecodeError:
            continue

        if (
            isinstance(action, dict)
            and "action" in action
            and "action_input" in action
        ):
            return action

    raise ValueError("No valid action JSON found in the response.")


def execute_action(action_data: dict) -> str:
    """
    Execute an action using the registered tools.
    """
    action_name = action_data["action"]
    action_input = action_data["action_input"]

    if action_name not in TOOL_REGISTRY:
        raise ValueError(f"Unknown or unauthorized tool: {action_name}")

    if not isinstance(action_input, dict):
        raise ValueError("action_input must be a dictionary.")

    tool_function = TOOL_REGISTRY[action_name]

    return tool_function(**action_input)
