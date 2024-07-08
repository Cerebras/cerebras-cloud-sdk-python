# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["PetFindByTagsParams"]


class PetFindByTagsParams(TypedDict, total=False):
    tags: List[str]
    """Tags to filter by"""
