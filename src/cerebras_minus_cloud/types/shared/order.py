# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Order"]


class Order(BaseModel):
    id: Optional[int] = None

    complete: Optional[bool] = None

    pet_id: Optional[int] = FieldInfo(alias="petId", default=None)

    quantity: Optional[int] = None

    ship_date: Optional[datetime] = FieldInfo(alias="shipDate", default=None)

    status: Optional[Literal["placed", "approved", "delivered"]] = None
    """Order Status"""
