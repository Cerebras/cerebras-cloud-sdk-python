# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ModelRetrieveParams"]


class ModelRetrieveParams(TypedDict, total=False):
    format: Literal["default", "openrouter", "huggingface"]
    """Output format: 'default' (OpenAI-compatible), 'openrouter', or 'huggingface'"""

    cf_ray: Annotated[str, PropertyInfo(alias="CF-RAY")]

    x_amz_cf_id: Annotated[str, PropertyInfo(alias="X-Amz-Cf-Id")]
