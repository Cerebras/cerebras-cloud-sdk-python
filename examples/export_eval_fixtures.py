"""Example: Exporting Cerebras chat completion responses as portable evaluation fixtures (#16)."""

import os
from typing import Any, Dict, List
from cerebras.cloud.sdk import Cerebras


def to_portable_eval_record(
    messages: List[Dict[str, str]],
    model: str,
    response: Any,
) -> Dict[str, Any]:
    """Convert a Cerebras ChatCompletion response into a portable eval fixture record."""
    choice = response.choices[0] if getattr(response, "choices", None) else None
    content = getattr(getattr(choice, "message", None), "content", None)
    usage_obj = getattr(response, "usage", None)
    usage = usage_obj.model_dump() if hasattr(usage_obj, "model_dump") else None
    return {
        "test_case_id": getattr(response, "id", None),
        "input": {"messages": messages},
        "actual_output": content,
        "metadata": {
            "model": model,
            "usage": usage,
        },
    }


def main() -> None:
    client = Cerebras(api_key=os.environ.get("CEREBRAS_API_KEY"))
    model = "llama3.1-8b"
    messages = [{"role": "user", "content": "Say hello in one sentence."}]
    response = client.chat.completions.create(model=model, messages=messages)
    record = to_portable_eval_record(messages, model, response)
    print(record)


if __name__ == "__main__":
    main()
