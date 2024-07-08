# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UserLoginParams"]


class UserLoginParams(TypedDict, total=False):
    password: str
    """The password for login in clear text"""

    username: str
    """The user name for login"""
