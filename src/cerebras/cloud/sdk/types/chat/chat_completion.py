# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
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
    "ChatCompletionResponseChoiceReasoningLogprobs",
    "ChatCompletionResponseChoiceReasoningLogprobsContent",
    "ChatCompletionResponseChoiceReasoningLogprobsContentTopLogprob",
    "ChatCompletionResponseChoiceReasoningLogprobsRefusal",
    "ChatCompletionResponseChoiceReasoningLogprobsRefusalTopLogprob",
    "ChatCompletionResponseTimeInfo",
    "ChatCompletionResponseUsage",
    "ChatCompletionResponseUsageCompletionTokensDetails",
    "ChatCompletionResponseUsagePromptTokensDetails",
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
    "ChatChunkResponseChoiceReasoningLogprobs",
    "ChatChunkResponseChoiceReasoningLogprobsContent",
    "ChatChunkResponseChoiceReasoningLogprobsContentTopLogprob",
    "ChatChunkResponseChoiceReasoningLogprobsRefusal",
    "ChatChunkResponseChoiceReasoningLogprobsRefusalTopLogprob",
    "ChatChunkResponseTimeInfo",
    "ChatChunkResponseUsage",
    "ChatChunkResponseUsageCompletionTokensDetails",
    "ChatChunkResponseUsagePromptTokensDetails",
    "ErrorChunkResponse",
    "ErrorChunkResponseError",
]


class ChatCompletionResponseChoiceMessageToolCallFunction(BaseModel):
    """Streaming only. Represents a function in an assistant tool call."""

    arguments: Optional[str] = None

    name: Optional[str] = None


class ChatCompletionResponseChoiceMessageToolCall(BaseModel):
    """Streaming only. Represents a function call in an assistant tool call."""

    function: ChatCompletionResponseChoiceMessageToolCallFunction
    """Streaming only. Represents a function in an assistant tool call."""

    type: Literal["function"]

    id: Optional[str] = None

    index: Optional[int] = None


class ChatCompletionResponseChoiceMessage(BaseModel):
    role: Literal["assistant", "user", "system", "tool"]

    content: Optional[str] = None

    reasoning: Optional[str] = None

    tool_calls: Optional[List[ChatCompletionResponseChoiceMessageToolCall]] = None


class ChatCompletionResponseChoiceLogprobsContentTopLogprob(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class ChatCompletionResponseChoiceLogprobsContent(BaseModel):
    token: str

    logprob: float

    top_logprobs: List[ChatCompletionResponseChoiceLogprobsContentTopLogprob]

    bytes: Optional[List[int]] = None


class ChatCompletionResponseChoiceLogprobsRefusalTopLogprob(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class ChatCompletionResponseChoiceLogprobsRefusal(BaseModel):
    token: str

    logprob: float

    top_logprobs: List[ChatCompletionResponseChoiceLogprobsRefusalTopLogprob]

    bytes: Optional[List[int]] = None


class ChatCompletionResponseChoiceLogprobs(BaseModel):
    content: Optional[List[ChatCompletionResponseChoiceLogprobsContent]] = None

    refusal: Optional[List[ChatCompletionResponseChoiceLogprobsRefusal]] = None


class ChatCompletionResponseChoiceReasoningLogprobsContentTopLogprob(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class ChatCompletionResponseChoiceReasoningLogprobsContent(BaseModel):
    token: str

    logprob: float

    top_logprobs: List[ChatCompletionResponseChoiceReasoningLogprobsContentTopLogprob]

    bytes: Optional[List[int]] = None


class ChatCompletionResponseChoiceReasoningLogprobsRefusalTopLogprob(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class ChatCompletionResponseChoiceReasoningLogprobsRefusal(BaseModel):
    token: str

    logprob: float

    top_logprobs: List[ChatCompletionResponseChoiceReasoningLogprobsRefusalTopLogprob]

    bytes: Optional[List[int]] = None


class ChatCompletionResponseChoiceReasoningLogprobs(BaseModel):
    content: Optional[List[ChatCompletionResponseChoiceReasoningLogprobsContent]] = None

    refusal: Optional[List[ChatCompletionResponseChoiceReasoningLogprobsRefusal]] = None


class ChatCompletionResponseChoice(BaseModel):
    index: int

    message: ChatCompletionResponseChoiceMessage

    finish_reason: Optional[Literal["stop", "length", "content_filter", "tool_calls"]] = None

    logprobs: Optional[ChatCompletionResponseChoiceLogprobs] = None

    reasoning_logprobs: Optional[ChatCompletionResponseChoiceReasoningLogprobs] = None


class ChatCompletionResponseTimeInfo(BaseModel):
    """Time information for different phases of request processing.

    All times are measured in seconds.
    """

    completion_time: Optional[float] = None

    created: Optional[float] = None

    prompt_time: Optional[float] = None

    queue_time: Optional[float] = None

    total_time: Optional[float] = None


class ChatCompletionResponseUsageCompletionTokensDetails(BaseModel):
    accepted_prediction_tokens: Optional[int] = None

    reasoning_tokens: Optional[int] = None

    rejected_prediction_tokens: Optional[int] = None


class ChatCompletionResponseUsagePromptTokensDetails(BaseModel):
    cached_tokens: Optional[int] = None


class ChatCompletionResponseUsage(BaseModel):
    completion_tokens: Optional[int] = None

    completion_tokens_details: Optional[ChatCompletionResponseUsageCompletionTokensDetails] = None

    image_tokens: Optional[int] = None

    prompt_tokens: Optional[int] = None

    prompt_tokens_details: Optional[ChatCompletionResponseUsagePromptTokensDetails] = None

    total_tokens: Optional[int] = None


class ChatCompletionResponse(BaseModel):
    id: str

    choices: List[ChatCompletionResponseChoice]

    created: int

    model: str

    object: Literal["chat.completion"]

    system_fingerprint: str

    service_tier: Optional[str] = None

    time_info: Optional[ChatCompletionResponseTimeInfo] = None
    """Time information for different phases of request processing.

    All times are measured in seconds.
    """

    usage: Optional[ChatCompletionResponseUsage] = None


class ChatChunkResponseChoiceDeltaToolCallFunction(BaseModel):
    """Streaming only. Represents a function in an assistant tool call."""

    arguments: Optional[str] = None

    name: Optional[str] = None


class ChatChunkResponseChoiceDeltaToolCall(BaseModel):
    """Streaming only. Represents a function call in an assistant tool call."""

    function: ChatChunkResponseChoiceDeltaToolCallFunction
    """Streaming only. Represents a function in an assistant tool call."""

    type: Literal["function"]

    id: Optional[str] = None

    index: Optional[int] = None


class ChatChunkResponseChoiceDelta(BaseModel):
    content: Optional[str] = None

    reasoning: Optional[str] = None

    role: Optional[Literal["assistant", "user", "system", "tool"]] = None

    tokens: Optional[List[int]] = None

    tool_calls: Optional[List[ChatChunkResponseChoiceDeltaToolCall]] = None


class ChatChunkResponseChoiceLogprobsContentTopLogprob(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class ChatChunkResponseChoiceLogprobsContent(BaseModel):
    token: str

    logprob: float

    top_logprobs: List[ChatChunkResponseChoiceLogprobsContentTopLogprob]

    bytes: Optional[List[int]] = None


class ChatChunkResponseChoiceLogprobsRefusalTopLogprob(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class ChatChunkResponseChoiceLogprobsRefusal(BaseModel):
    token: str

    logprob: float

    top_logprobs: List[ChatChunkResponseChoiceLogprobsRefusalTopLogprob]

    bytes: Optional[List[int]] = None


class ChatChunkResponseChoiceLogprobs(BaseModel):
    content: Optional[List[ChatChunkResponseChoiceLogprobsContent]] = None

    refusal: Optional[List[ChatChunkResponseChoiceLogprobsRefusal]] = None


class ChatChunkResponseChoiceReasoningLogprobsContentTopLogprob(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class ChatChunkResponseChoiceReasoningLogprobsContent(BaseModel):
    token: str

    logprob: float

    top_logprobs: List[ChatChunkResponseChoiceReasoningLogprobsContentTopLogprob]

    bytes: Optional[List[int]] = None


class ChatChunkResponseChoiceReasoningLogprobsRefusalTopLogprob(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class ChatChunkResponseChoiceReasoningLogprobsRefusal(BaseModel):
    token: str

    logprob: float

    top_logprobs: List[ChatChunkResponseChoiceReasoningLogprobsRefusalTopLogprob]

    bytes: Optional[List[int]] = None


class ChatChunkResponseChoiceReasoningLogprobs(BaseModel):
    content: Optional[List[ChatChunkResponseChoiceReasoningLogprobsContent]] = None

    refusal: Optional[List[ChatChunkResponseChoiceReasoningLogprobsRefusal]] = None


class ChatChunkResponseChoice(BaseModel):
    index: int

    delta: Optional[ChatChunkResponseChoiceDelta] = None

    finish_reason: Optional[Literal["stop", "length", "content_filter", "tool_calls"]] = None

    logprobs: Optional[ChatChunkResponseChoiceLogprobs] = None

    reasoning_logprobs: Optional[ChatChunkResponseChoiceReasoningLogprobs] = None

    text: Optional[str] = None

    tokens: Optional[List[int]] = None


class ChatChunkResponseTimeInfo(BaseModel):
    """Time information for different phases of request processing.

    All times are measured in seconds.
    """

    completion_time: Optional[float] = None

    created: Optional[float] = None

    prompt_time: Optional[float] = None

    queue_time: Optional[float] = None

    total_time: Optional[float] = None


class ChatChunkResponseUsageCompletionTokensDetails(BaseModel):
    accepted_prediction_tokens: Optional[int] = None

    reasoning_tokens: Optional[int] = None

    rejected_prediction_tokens: Optional[int] = None


class ChatChunkResponseUsagePromptTokensDetails(BaseModel):
    cached_tokens: Optional[int] = None


class ChatChunkResponseUsage(BaseModel):
    completion_tokens: Optional[int] = None

    completion_tokens_details: Optional[ChatChunkResponseUsageCompletionTokensDetails] = None

    image_tokens: Optional[int] = None

    prompt_tokens: Optional[int] = None

    prompt_tokens_details: Optional[ChatChunkResponseUsagePromptTokensDetails] = None

    total_tokens: Optional[int] = None


class ChatChunkResponse(BaseModel):
    id: str

    created: int

    model: str

    object: Literal["chat.completion.chunk"]

    system_fingerprint: str

    choices: Optional[List[ChatChunkResponseChoice]] = None

    service_tier: Optional[str] = None

    time_info: Optional[ChatChunkResponseTimeInfo] = None
    """Time information for different phases of request processing.

    All times are measured in seconds.
    """

    usage: Optional[ChatChunkResponseUsage] = None


class ErrorChunkResponseError(BaseModel):
    id: Optional[str] = None

    code: Optional[str] = None

    message: Optional[str] = None

    param: Optional[str] = None

    type: Optional[str] = None


class ErrorChunkResponse(BaseModel):
    error: ErrorChunkResponseError

    status_code: int


ChatCompletion: TypeAlias = Union[ChatCompletionResponse, ChatChunkResponse, ErrorChunkResponse]

# This was the name of the union type prior to 1.12.0, so we will alias it here
# to ensure any existing code won't break.
CompletionCreateResponse: TypeAlias = ChatCompletion
