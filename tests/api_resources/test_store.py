# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from cerebras_minus_cloud import Petstore, AsyncPetstore
from cerebras_minus_cloud.types import StoreInventoryResponse
from cerebras_minus_cloud._utils import parse_datetime
from cerebras_minus_cloud.types.shared import Order

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStore:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_order(self, client: Petstore) -> None:
        store = client.store.create_order()
        assert_matches_type(Order, store, path=["response"])

    @parametrize
    def test_method_create_order_with_all_params(self, client: Petstore) -> None:
        store = client.store.create_order(
            id=10,
            complete=True,
            pet_id=198772,
            quantity=7,
            ship_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="approved",
        )
        assert_matches_type(Order, store, path=["response"])

    @parametrize
    def test_raw_response_create_order(self, client: Petstore) -> None:
        response = client.store.with_raw_response.create_order()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        store = response.parse()
        assert_matches_type(Order, store, path=["response"])

    @parametrize
    def test_streaming_response_create_order(self, client: Petstore) -> None:
        with client.store.with_streaming_response.create_order() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            store = response.parse()
            assert_matches_type(Order, store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_inventory(self, client: Petstore) -> None:
        store = client.store.inventory()
        assert_matches_type(StoreInventoryResponse, store, path=["response"])

    @parametrize
    def test_raw_response_inventory(self, client: Petstore) -> None:
        response = client.store.with_raw_response.inventory()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        store = response.parse()
        assert_matches_type(StoreInventoryResponse, store, path=["response"])

    @parametrize
    def test_streaming_response_inventory(self, client: Petstore) -> None:
        with client.store.with_streaming_response.inventory() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            store = response.parse()
            assert_matches_type(StoreInventoryResponse, store, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStore:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_order(self, async_client: AsyncPetstore) -> None:
        store = await async_client.store.create_order()
        assert_matches_type(Order, store, path=["response"])

    @parametrize
    async def test_method_create_order_with_all_params(self, async_client: AsyncPetstore) -> None:
        store = await async_client.store.create_order(
            id=10,
            complete=True,
            pet_id=198772,
            quantity=7,
            ship_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="approved",
        )
        assert_matches_type(Order, store, path=["response"])

    @parametrize
    async def test_raw_response_create_order(self, async_client: AsyncPetstore) -> None:
        response = await async_client.store.with_raw_response.create_order()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        store = await response.parse()
        assert_matches_type(Order, store, path=["response"])

    @parametrize
    async def test_streaming_response_create_order(self, async_client: AsyncPetstore) -> None:
        async with async_client.store.with_streaming_response.create_order() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            store = await response.parse()
            assert_matches_type(Order, store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_inventory(self, async_client: AsyncPetstore) -> None:
        store = await async_client.store.inventory()
        assert_matches_type(StoreInventoryResponse, store, path=["response"])

    @parametrize
    async def test_raw_response_inventory(self, async_client: AsyncPetstore) -> None:
        response = await async_client.store.with_raw_response.inventory()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        store = await response.parse()
        assert_matches_type(StoreInventoryResponse, store, path=["response"])

    @parametrize
    async def test_streaming_response_inventory(self, async_client: AsyncPetstore) -> None:
        async with async_client.store.with_streaming_response.inventory() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            store = await response.parse()
            assert_matches_type(StoreInventoryResponse, store, path=["response"])

        assert cast(Any, response.is_closed) is True
