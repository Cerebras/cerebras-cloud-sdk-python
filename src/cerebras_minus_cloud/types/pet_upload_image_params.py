# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["PetUploadImageParams"]


class PetUploadImageParams(TypedDict, total=False):
    image: Required[FileTypes]

    additional_metadata: Annotated[str, PropertyInfo(alias="additionalMetadata")]
    """Additional Metadata"""
