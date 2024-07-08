# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from .order import (
    OrderResource,
    AsyncOrderResource,
    OrderResourceWithRawResponse,
    AsyncOrderResourceWithRawResponse,
    OrderResourceWithStreamingResponse,
    AsyncOrderResourceWithStreamingResponse,
)
from ...types import store_create_order_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import (
    make_request_options,
)
from ...types.shared.order import Order
from ...types.store_inventory_response import StoreInventoryResponse

__all__ = ["StoreResource", "AsyncStoreResource"]


class StoreResource(SyncAPIResource):
    @cached_property
    def order(self) -> OrderResource:
        return OrderResource(self._client)

    @cached_property
    def with_raw_response(self) -> StoreResourceWithRawResponse:
        return StoreResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StoreResourceWithStreamingResponse:
        return StoreResourceWithStreamingResponse(self)

    def create_order(
        self,
        *,
        id: int | NotGiven = NOT_GIVEN,
        complete: bool | NotGiven = NOT_GIVEN,
        pet_id: int | NotGiven = NOT_GIVEN,
        quantity: int | NotGiven = NOT_GIVEN,
        ship_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        status: Literal["placed", "approved", "delivered"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Order:
        """
        Place a new order in the store

        Args:
          status: Order Status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/store/order",
            body=maybe_transform(
                {
                    "id": id,
                    "complete": complete,
                    "pet_id": pet_id,
                    "quantity": quantity,
                    "ship_date": ship_date,
                    "status": status,
                },
                store_create_order_params.StoreCreateOrderParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Order,
        )

    def inventory(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StoreInventoryResponse:
        """Returns a map of status codes to quantities"""
        return self._get(
            "/store/inventory",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StoreInventoryResponse,
        )


class AsyncStoreResource(AsyncAPIResource):
    @cached_property
    def order(self) -> AsyncOrderResource:
        return AsyncOrderResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncStoreResourceWithRawResponse:
        return AsyncStoreResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStoreResourceWithStreamingResponse:
        return AsyncStoreResourceWithStreamingResponse(self)

    async def create_order(
        self,
        *,
        id: int | NotGiven = NOT_GIVEN,
        complete: bool | NotGiven = NOT_GIVEN,
        pet_id: int | NotGiven = NOT_GIVEN,
        quantity: int | NotGiven = NOT_GIVEN,
        ship_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        status: Literal["placed", "approved", "delivered"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Order:
        """
        Place a new order in the store

        Args:
          status: Order Status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/store/order",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "complete": complete,
                    "pet_id": pet_id,
                    "quantity": quantity,
                    "ship_date": ship_date,
                    "status": status,
                },
                store_create_order_params.StoreCreateOrderParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Order,
        )

    async def inventory(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StoreInventoryResponse:
        """Returns a map of status codes to quantities"""
        return await self._get(
            "/store/inventory",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StoreInventoryResponse,
        )


class StoreResourceWithRawResponse:
    def __init__(self, store: StoreResource) -> None:
        self._store = store

        self.create_order = to_raw_response_wrapper(
            store.create_order,
        )
        self.inventory = to_raw_response_wrapper(
            store.inventory,
        )

    @cached_property
    def order(self) -> OrderResourceWithRawResponse:
        return OrderResourceWithRawResponse(self._store.order)


class AsyncStoreResourceWithRawResponse:
    def __init__(self, store: AsyncStoreResource) -> None:
        self._store = store

        self.create_order = async_to_raw_response_wrapper(
            store.create_order,
        )
        self.inventory = async_to_raw_response_wrapper(
            store.inventory,
        )

    @cached_property
    def order(self) -> AsyncOrderResourceWithRawResponse:
        return AsyncOrderResourceWithRawResponse(self._store.order)


class StoreResourceWithStreamingResponse:
    def __init__(self, store: StoreResource) -> None:
        self._store = store

        self.create_order = to_streamed_response_wrapper(
            store.create_order,
        )
        self.inventory = to_streamed_response_wrapper(
            store.inventory,
        )

    @cached_property
    def order(self) -> OrderResourceWithStreamingResponse:
        return OrderResourceWithStreamingResponse(self._store.order)


class AsyncStoreResourceWithStreamingResponse:
    def __init__(self, store: AsyncStoreResource) -> None:
        self._store = store

        self.create_order = async_to_streamed_response_wrapper(
            store.create_order,
        )
        self.inventory = async_to_streamed_response_wrapper(
            store.inventory,
        )

    @cached_property
    def order(self) -> AsyncOrderResourceWithStreamingResponse:
        return AsyncOrderResourceWithStreamingResponse(self._store.order)
