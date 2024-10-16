# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import TYPE_CHECKING, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .chat_completion import ChatCompletion

__all__ = [
    "CompletionCreateResponse",
    "ChatChunkResponse",
    "ChatChunkResponseChoice",
    "ChatChunkResponseChoiceDelta",
    "ChatChunkResponseChoiceDeltaToolCall",
    "ChatChunkResponseChoiceDeltaToolCallFunction",
    "ChatChunkResponseChoiceLogprobs",
    "ChatChunkResponseChoiceLogprobsContent",
    "ChatChunkResponseChoiceLogprobsContentTopLogprobs",
    "ChatChunkResponseTimeInfo",
    "ChatChunkResponseUsage",
    "ErrorChunkResponse",
    "ErrorChunkResponseError",
]


class ChatChunkResponseChoiceDeltaToolCallFunction(BaseModel):
    arguments: str

    name: str

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ChatChunkResponseChoiceDeltaToolCall(BaseModel):
    id: str

    function: ChatChunkResponseChoiceDeltaToolCallFunction

    type: Literal["function"]

    index: Optional[int] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ChatChunkResponseChoiceDelta(BaseModel):
    content: Optional[str] = None

    role: Optional[Literal["assistant", "user", "system", "tool"]] = None

    tool_calls: Optional[List[ChatChunkResponseChoiceDeltaToolCall]] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ChatChunkResponseChoiceLogprobsContentTopLogprobs(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ChatChunkResponseChoiceLogprobsContent(BaseModel):
    token: str

    logprob: float

    top_logprobs: ChatChunkResponseChoiceLogprobsContentTopLogprobs

    bytes: Optional[List[int]] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ChatChunkResponseChoiceLogprobs(BaseModel):
    content: ChatChunkResponseChoiceLogprobsContent

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ChatChunkResponseChoice(BaseModel):
    delta: ChatChunkResponseChoiceDelta

    index: int

    finish_reason: Optional[Literal["stop", "length", "content_filter", "tool_calls"]] = None

    logprobs: Optional[ChatChunkResponseChoiceLogprobs] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ChatChunkResponseTimeInfo(BaseModel):
    completion_time: Optional[float] = None

    prompt_time: Optional[float] = None

    queue_time: Optional[float] = None

    total_time: Optional[float] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ChatChunkResponseUsage(BaseModel):
    completion_tokens: Optional[int] = None

    prompt_tokens: Optional[int] = None

    total_tokens: Optional[int] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ChatChunkResponse(BaseModel):
    id: str

    created: int

    model: str

    object: Literal["chat.completion.chunk"]

    system_fingerprint: str

    choices: Optional[List[ChatChunkResponseChoice]] = None

    service_tier: Optional[str] = None

    time_info: Optional[ChatChunkResponseTimeInfo] = None

    usage: Optional[ChatChunkResponseUsage] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> builtins.object: ...


class ErrorChunkResponseError(BaseModel):
    code: Optional[str] = None

    message: Optional[str] = None

    param: Optional[str] = None

    type: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ErrorChunkResponse(BaseModel):
    error: ErrorChunkResponseError

    status_code: int

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


CompletionCreateResponse: TypeAlias = Union[ChatCompletion, ChatChunkResponse, ErrorChunkResponse]
