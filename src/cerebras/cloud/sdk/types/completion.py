# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "Completion",
    "CompletionResponse",
    "CompletionResponseChoice",
    "CompletionResponseChoiceLogprobs",
    "CompletionResponseTimeInfo",
    "CompletionResponseUsage",
    "CompletionResponseUsageCompletionTokensDetails",
    "CompletionResponseUsagePromptTokensDetails",
    "ErrorChunkResponse",
    "ErrorChunkResponseError",
]


class CompletionResponseChoiceLogprobs(BaseModel):
    text_offset: Optional[List[int]] = None

    token_logprobs: Optional[List[float]] = None

    tokens: Optional[List[str]] = None

    top_logprobs: Optional[List[Dict[str, float]]] = None


class CompletionResponseChoice(BaseModel):
    index: int

    finish_reason: Optional[Literal["stop", "length", "content_filter", "tool_calls"]] = None

    logprobs: Optional[CompletionResponseChoiceLogprobs] = None

    text: Optional[str] = None

    tokens: Optional[List[int]] = None


class CompletionResponseTimeInfo(BaseModel):
    """Time information for different phases of request processing.

    All times are measured in seconds.
    """

    completion_time: Optional[float] = None

    created: Optional[float] = None

    prompt_time: Optional[float] = None

    queue_time: Optional[float] = None

    total_time: Optional[float] = None


class CompletionResponseUsageCompletionTokensDetails(BaseModel):
    accepted_prediction_tokens: Optional[int] = None

    reasoning_tokens: Optional[int] = None

    rejected_prediction_tokens: Optional[int] = None


class CompletionResponseUsagePromptTokensDetails(BaseModel):
    cached_tokens: Optional[int] = None


class CompletionResponseUsage(BaseModel):
    completion_tokens: Optional[int] = None

    completion_tokens_details: Optional[CompletionResponseUsageCompletionTokensDetails] = None

    image_tokens: Optional[int] = None

    prompt_tokens: Optional[int] = None

    prompt_tokens_details: Optional[CompletionResponseUsagePromptTokensDetails] = None

    total_tokens: Optional[int] = None


class CompletionResponse(BaseModel):
    id: str

    choices: List[CompletionResponseChoice]

    created: int

    model: str

    object: Literal["text_completion"]

    system_fingerprint: str

    time_info: Optional[CompletionResponseTimeInfo] = None
    """Time information for different phases of request processing.

    All times are measured in seconds.
    """

    usage: Optional[CompletionResponseUsage] = None


class ErrorChunkResponseError(BaseModel):
    id: Optional[str] = None

    code: Optional[str] = None

    message: Optional[str] = None

    param: Optional[str] = None

    type: Optional[str] = None


class ErrorChunkResponse(BaseModel):
    error: ErrorChunkResponseError

    status_code: int


Completion: TypeAlias = Union[CompletionResponse, ErrorChunkResponse]
