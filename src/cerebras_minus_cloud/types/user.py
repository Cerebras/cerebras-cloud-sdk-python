# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["User"]


class User(BaseModel):
    id: Optional[int] = None

    email: Optional[str] = None

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)

    password: Optional[str] = None

    phone: Optional[str] = None

    username: Optional[str] = None

    user_status: Optional[int] = FieldInfo(alias="userStatus", default=None)
    """User Status"""
