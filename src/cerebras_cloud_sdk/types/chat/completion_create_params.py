# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CompletionCreateParams", "Message"]


class CompletionCreateParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]

    model: Required[Literal["llama3-8b-8192"]]

    max_tokens: int

    prompt: str

    seed: int

    stop_sequence: str

    stream: bool

    temperature: float

    top_p: float


class Message(TypedDict, total=False):
    role: Required[Literal["user", "assistant"]]

    content: str
