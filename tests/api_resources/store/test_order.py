# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from cerebras_minus_cloud import Petstore, AsyncPetstore
from cerebras_minus_cloud.types.shared import Order

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrder:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Petstore) -> None:
        order = client.store.order.retrieve(
            0,
        )
        assert_matches_type(Order, order, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Petstore) -> None:
        response = client.store.order.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(Order, order, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Petstore) -> None:
        with client.store.order.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(Order, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete_order(self, client: Petstore) -> None:
        order = client.store.order.delete_order(
            0,
        )
        assert order is None

    @parametrize
    def test_raw_response_delete_order(self, client: Petstore) -> None:
        response = client.store.order.with_raw_response.delete_order(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert order is None

    @parametrize
    def test_streaming_response_delete_order(self, client: Petstore) -> None:
        with client.store.order.with_streaming_response.delete_order(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert order is None

        assert cast(Any, response.is_closed) is True


class TestAsyncOrder:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPetstore) -> None:
        order = await async_client.store.order.retrieve(
            0,
        )
        assert_matches_type(Order, order, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPetstore) -> None:
        response = await async_client.store.order.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(Order, order, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPetstore) -> None:
        async with async_client.store.order.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(Order, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete_order(self, async_client: AsyncPetstore) -> None:
        order = await async_client.store.order.delete_order(
            0,
        )
        assert order is None

    @parametrize
    async def test_raw_response_delete_order(self, async_client: AsyncPetstore) -> None:
        response = await async_client.store.order.with_raw_response.delete_order(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert order is None

    @parametrize
    async def test_streaming_response_delete_order(self, async_client: AsyncPetstore) -> None:
        async with async_client.store.order.with_streaming_response.delete_order(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert order is None

        assert cast(Any, response.is_closed) is True
