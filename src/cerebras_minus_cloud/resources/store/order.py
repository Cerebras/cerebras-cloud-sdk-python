# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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

__all__ = ["OrderResource", "AsyncOrderResource"]


class OrderResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OrderResourceWithRawResponse:
        return OrderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrderResourceWithStreamingResponse:
        return OrderResourceWithStreamingResponse(self)

    def retrieve(
        self,
        order_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Order:
        """For valid response try integer IDs with value <= 5 or > 10.

        Other values will
        generate exceptions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/store/order/{order_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Order,
        )

    def delete_order(
        self,
        order_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """For valid response try integer IDs with value < 1000.

        Anything above 1000 or
        nonintegers will generate API errors

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/store/order/{order_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncOrderResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOrderResourceWithRawResponse:
        return AsyncOrderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrderResourceWithStreamingResponse:
        return AsyncOrderResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        order_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Order:
        """For valid response try integer IDs with value <= 5 or > 10.

        Other values will
        generate exceptions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/store/order/{order_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Order,
        )

    async def delete_order(
        self,
        order_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """For valid response try integer IDs with value < 1000.

        Anything above 1000 or
        nonintegers will generate API errors

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/store/order/{order_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class OrderResourceWithRawResponse:
    def __init__(self, order: OrderResource) -> None:
        self._order = order

        self.retrieve = to_raw_response_wrapper(
            order.retrieve,
        )
        self.delete_order = to_raw_response_wrapper(
            order.delete_order,
        )


class AsyncOrderResourceWithRawResponse:
    def __init__(self, order: AsyncOrderResource) -> None:
        self._order = order

        self.retrieve = async_to_raw_response_wrapper(
            order.retrieve,
        )
        self.delete_order = async_to_raw_response_wrapper(
            order.delete_order,
        )


class OrderResourceWithStreamingResponse:
    def __init__(self, order: OrderResource) -> None:
        self._order = order

        self.retrieve = to_streamed_response_wrapper(
            order.retrieve,
        )
        self.delete_order = to_streamed_response_wrapper(
            order.delete_order,
        )


class AsyncOrderResourceWithStreamingResponse:
    def __init__(self, order: AsyncOrderResource) -> None:
        self._order = order

        self.retrieve = async_to_streamed_response_wrapper(
            order.retrieve,
        )
        self.delete_order = async_to_streamed_response_wrapper(
            order.delete_order,
        )
