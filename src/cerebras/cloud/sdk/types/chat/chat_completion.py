# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "ChatCompletion",
    "Choice",
    "ChoiceMessage",
    "ChoiceLogprobs",
    "ChoiceLogprobsContent",
    "ChoiceLogprobsContentTopLogprobs",
    "TimeInfo",
    "Usage",
]


class ChoiceMessage(BaseModel):
    role: Literal["assistant"]

    content: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object:
            ...


class ChoiceLogprobsContentTopLogprobs(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class ChoiceLogprobsContent(BaseModel):
    token: str

    logprob: float

    top_logprobs: ChoiceLogprobsContentTopLogprobs

    bytes: Optional[List[int]] = None


class ChoiceLogprobs(BaseModel):
    content: ChoiceLogprobsContent


class Choice(BaseModel):
    finish_reason: Literal["stop", "length", "content_filter", "tool_calls"]

    index: int

    message: ChoiceMessage

    logprobs: Optional[ChoiceLogprobs] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object:
            ...


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

    model: Literal["llama3-8b-8192", "llama3-70b-8192"]

    object: Literal["chat.completion"]

    system_fingerprint: str

    time_info: TimeInfo

    usage: Usage
