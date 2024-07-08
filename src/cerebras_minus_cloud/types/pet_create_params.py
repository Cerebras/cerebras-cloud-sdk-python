# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PetCreateParams", "Category", "Tag"]


class PetCreateParams(TypedDict, total=False):
    name: Required[str]

    photo_urls: Required[Annotated[List[str], PropertyInfo(alias="photoUrls")]]

    id: int

    category: Category

    status: Literal["available", "pending", "sold"]
    """pet status in the store"""

    tags: Iterable[Tag]


class Category(TypedDict, total=False):
    id: int

    name: str


class Tag(TypedDict, total=False):
    id: int

    name: str
