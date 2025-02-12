# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "Completion",
    "CompletionResponse",
    "CompletionResponseChoice",
    "CompletionResponseChoiceLogprobs",
    "CompletionResponseTimeInfo",
    "CompletionResponseUsage",
    "ErrorChunkResponse",
    "ErrorChunkResponseError",
]


class CompletionResponseChoiceLogprobs(BaseModel):
    text_offset: Optional[List[int]] = None

    token_logprobs: Optional[List[float]] = None

    tokens: Optional[List[str]] = None

    top_logprobs: Optional[List[Dict[str, float]]] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class CompletionResponseChoice(BaseModel):
    index: int

    finish_reason: Optional[Literal["stop", "length", "content_filter"]] = None

    logprobs: Optional[CompletionResponseChoiceLogprobs] = None

    text: Optional[str] = None

    tokens: Optional[List[int]] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class CompletionResponseTimeInfo(BaseModel):
    completion_time: Optional[float] = None

    prompt_time: Optional[float] = None

    queue_time: Optional[float] = None

    total_time: Optional[float] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class CompletionResponseUsage(BaseModel):
    completion_tokens: Optional[int] = None

    prompt_tokens: Optional[int] = None

    total_tokens: Optional[int] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class CompletionResponse(BaseModel):
    id: str

    choices: List[CompletionResponseChoice]

    created: int

    model: str

    object: Literal["text_completion"]

    system_fingerprint: str

    time_info: Optional[CompletionResponseTimeInfo] = None

    usage: Optional[CompletionResponseUsage] = None

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


Completion: TypeAlias = Union[CompletionResponse, ErrorChunkResponse]
