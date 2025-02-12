# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import TYPE_CHECKING, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "ChatCompletion",
    "ChatCompletionResponse",
    "ChatCompletionResponseChoice",
    "ChatCompletionResponseChoiceMessage",
    "ChatCompletionResponseChoiceMessageToolCall",
    "ChatCompletionResponseChoiceMessageToolCallFunction",
    "ChatCompletionResponseChoiceLogprobs",
    "ChatCompletionResponseChoiceLogprobsContent",
    "ChatCompletionResponseChoiceLogprobsContentTopLogprob",
    "ChatCompletionResponseChoiceLogprobsRefusal",
    "ChatCompletionResponseChoiceLogprobsRefusalTopLogprob",
    "ChatCompletionResponseTimeInfo",
    "ChatCompletionResponseUsage",
    "ChatChunkResponse",
    "ChatChunkResponseChoice",
    "ChatChunkResponseChoiceDelta",
    "ChatChunkResponseChoiceDeltaToolCall",
    "ChatChunkResponseChoiceDeltaToolCallFunction",
    "ChatChunkResponseChoiceLogprobs",
    "ChatChunkResponseChoiceLogprobsContent",
    "ChatChunkResponseChoiceLogprobsContentTopLogprob",
    "ChatChunkResponseChoiceLogprobsRefusal",
    "ChatChunkResponseChoiceLogprobsRefusalTopLogprob",
    "ChatChunkResponseTimeInfo",
    "ChatChunkResponseUsage",
    "ErrorChunkResponse",
    "ErrorChunkResponseError",
]


class ChatCompletionResponseChoiceMessageToolCallFunction(BaseModel):
    arguments: str

    name: str

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ChatCompletionResponseChoiceMessageToolCall(BaseModel):
    id: str

    function: ChatCompletionResponseChoiceMessageToolCallFunction

    type: Literal["function"]

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ChatCompletionResponseChoiceMessage(BaseModel):
    role: Literal["assistant", "user", "system", "tool"]

    content: Optional[str] = None

    tool_calls: Optional[List[ChatCompletionResponseChoiceMessageToolCall]] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ChatCompletionResponseChoiceLogprobsContentTopLogprob(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ChatCompletionResponseChoiceLogprobsContent(BaseModel):
    token: str

    logprob: float

    top_logprobs: List[ChatCompletionResponseChoiceLogprobsContentTopLogprob]

    bytes: Optional[List[int]] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ChatCompletionResponseChoiceLogprobsRefusalTopLogprob(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ChatCompletionResponseChoiceLogprobsRefusal(BaseModel):
    token: str

    logprob: float

    top_logprobs: List[ChatCompletionResponseChoiceLogprobsRefusalTopLogprob]

    bytes: Optional[List[int]] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ChatCompletionResponseChoiceLogprobs(BaseModel):
    content: Optional[List[ChatCompletionResponseChoiceLogprobsContent]] = None

    refusal: Optional[List[ChatCompletionResponseChoiceLogprobsRefusal]] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ChatCompletionResponseChoice(BaseModel):
    finish_reason: Literal["stop", "length", "content_filter", "tool_calls"]

    index: int

    message: ChatCompletionResponseChoiceMessage

    logprobs: Optional[ChatCompletionResponseChoiceLogprobs] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ChatCompletionResponseTimeInfo(BaseModel):
    completion_time: Optional[float] = None

    prompt_time: Optional[float] = None

    queue_time: Optional[float] = None

    total_time: Optional[float] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ChatCompletionResponseUsage(BaseModel):
    completion_tokens: Optional[int] = None

    prompt_tokens: Optional[int] = None

    total_tokens: Optional[int] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ChatCompletionResponse(BaseModel):
    id: str

    choices: List[ChatCompletionResponseChoice]

    created: int

    model: str

    object: Literal["chat.completion"]

    system_fingerprint: str

    time_info: ChatCompletionResponseTimeInfo

    usage: ChatCompletionResponseUsage

    service_tier: Optional[str] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> builtins.object: ...


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


class ChatChunkResponseChoiceLogprobsContentTopLogprob(BaseModel):
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

    top_logprobs: List[ChatChunkResponseChoiceLogprobsContentTopLogprob]

    bytes: Optional[List[int]] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ChatChunkResponseChoiceLogprobsRefusalTopLogprob(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ChatChunkResponseChoiceLogprobsRefusal(BaseModel):
    token: str

    logprob: float

    top_logprobs: List[ChatChunkResponseChoiceLogprobsRefusalTopLogprob]

    bytes: Optional[List[int]] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ChatChunkResponseChoiceLogprobs(BaseModel):
    content: Optional[List[ChatChunkResponseChoiceLogprobsContent]] = None

    refusal: Optional[List[ChatChunkResponseChoiceLogprobsRefusal]] = None

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


ChatCompletion: TypeAlias = Union[ChatCompletionResponse, ChatChunkResponse, ErrorChunkResponse]

# This was the name of the union type prior to 1.12.0, so we will alias it here
# to ensure any existing code won't break.
CompletionCreateResponse: TypeAlias = ChatCompletion
