# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ChatCompletion", "Choice", "ChoiceMessage", "TimeInfo", "Usage"]


class ChoiceMessage(BaseModel):
    role: Literal["assistant"]

    content: Optional[str] = None


class Choice(BaseModel):
    finish_reason: Literal["stop", "length", "content_filter", "tool_calls"]

    index: int

    message: ChoiceMessage


class TimeInfo(BaseModel):
    completion_time: Optional[float] = None

    prompt_time: Optional[float] = None

    queue_time: Optional[float] = None

    total_time: Optional[float] = None


class Usage(BaseModel):
    completion_tokens: Optional[int] = None

    prompt_tokens: Optional[int] = None

    total_tokens: Optional[int] = None


class ChatCompletion(BaseModel):
    id: str

    choices: List[Choice]

    created: int

    model: Literal["llama3-8b-8192"]

    object: Literal["chat.completion"]

    system_fingerprint: str

    time_info: TimeInfo

    usage: Usage
