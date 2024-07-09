# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CompletionCreateParams", "Message"]


class CompletionCreateParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]

    model: Required[Literal["llama3-8b-8192"]]

    max_tokens: int
    """
    The maximum number of [tokens](/tokenizer) that can be generated in the
    completion. The token count of your prompt plus `max_tokens` cannot exceed the
    model's context length.
    """

    prompt: str

    seed: int
    """
    If specified, our system will make a best effort to sample deterministically,
    such that repeated requests with the same `seed` and parameters should return
    the same result. Determinism is not guaranteed.
    """

    stop_sequence: str
    """Up to 4 sequences where the API will stop generating further tokens.

    The returned text will not contain the stop sequence.
    """

    stream: bool

    temperature: float
    """What sampling temperature to use, between 0 and 2.

    Higher values like 0.8 will make the output more random, while lower values like
    0.2 will make it more focused and deterministic. We generally recommend altering
    this or `top_p` but not both.
    """

    top_p: float
    """
    An alternative to sampling with temperature, called nucleus sampling, where the
    model considers the results of the tokens with top_p probability mass. So 0.1
    means only the tokens comprising the top 10% probability mass are considered. We
    generally recommend altering this or `temperature` but not both.
    """


class Message(TypedDict, total=False):
    role: Required[Literal["user", "assistant"]]

    content: str
