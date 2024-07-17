# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .chat_completion import ChatCompletion

__all__ = [
    "CompletionCreateResponse",
    "ChatChunkResponse",
    "ChatChunkResponseChoice",
    "ChatChunkResponseChoiceDelta",
    "ChatChunkResponseTimeInfo",
    "ChatChunkResponseUsage",
    "ErrorChunkResponse",
    "ErrorChunkResponseContent",
]


class ChatChunkResponseChoiceDelta(BaseModel):
    content: Optional[str] = None

    role: Optional[Literal["assistant"]] = None


class ChatChunkResponseChoice(BaseModel):
    delta: ChatChunkResponseChoiceDelta

    index: int

    finish_reason: Optional[Literal["stop", "length", "content_filter", "tool_calls"]] = None


class ChatChunkResponseTimeInfo(BaseModel):
    completion_time: Optional[float] = None

    prompt_time: Optional[float] = None

    queue_time: Optional[float] = None

    total_time: Optional[float] = None


class ChatChunkResponseUsage(BaseModel):
    completion_tokens: Optional[int] = None

    prompt_tokens: Optional[int] = None

    total_tokens: Optional[int] = None


class ChatChunkResponse(BaseModel):
    id: str

    choices: List[ChatChunkResponseChoice]

    created: int

    model: Literal["llama3-8b-8192"]

    object: Literal["chat.completion.chunk"]

    system_fingerprint: str

    time_info: Optional[ChatChunkResponseTimeInfo] = None

    usage: Optional[ChatChunkResponseUsage] = None


class ErrorChunkResponseContent(BaseModel):
    code: Optional[str] = None

    message: Optional[str] = None

    param: Optional[str] = None

    type: Optional[str] = None


class ErrorChunkResponse(BaseModel):
    content: ErrorChunkResponseContent

    status_code: int


CompletionCreateResponse = Union[ChatCompletion, ChatChunkResponse, ErrorChunkResponse]
