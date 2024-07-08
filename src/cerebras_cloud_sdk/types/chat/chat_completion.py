# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ChatCompletion", "Message", "TimeInfo", "TokenInfo"]


class Message(BaseModel):
    role: Literal["user", "assistant"]

    content: Optional[str] = None


class TimeInfo(BaseModel):
    input_inference_time: Optional[int] = None

    output_inference_time: Optional[int] = None

    start_time: Optional[int] = None

    total_inference_time: Optional[int] = None


class TokenInfo(BaseModel):
    input_tokens: Optional[int] = None

    output_tokens: Optional[int] = None

    total_tokens: Optional[int] = None


class ChatCompletion(BaseModel):
    messages: List[Message]

    model: str

    time_info: TimeInfo

    token_info: TokenInfo
