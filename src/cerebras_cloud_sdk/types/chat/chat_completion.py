# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ChatCompletion", "Message", "TimeInfo", "Usage"]


class Message(BaseModel):
    role: object

    content: Optional[str] = None


class TimeInfo(BaseModel):
    completion_time: Optional[float] = None

    creation: Optional[int] = None

    prompt_time: Optional[float] = None

    queue_time: Optional[float] = None

    total_time: Optional[float] = None


class Usage(BaseModel):
    completion_tokens: Optional[int] = None

    prompt_tokens: Optional[int] = None

    total_tokens: Optional[int] = None


class ChatCompletion(BaseModel):
    messages: List[Message]

    model: Literal["llama3-8b-8192"]

    finish_reason: Optional[object] = None

    time_info: Optional[TimeInfo] = None

    usage: Optional[Usage] = None
