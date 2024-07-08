# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .user_param import UserParam

__all__ = ["UserCreateWithListParams"]


class UserCreateWithListParams(TypedDict, total=False):
    items: Required[Iterable[UserParam]]
