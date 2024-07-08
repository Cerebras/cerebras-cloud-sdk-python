# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from cerebras_minus_cloud import Petstore, AsyncPetstore
from cerebras_minus_cloud.types import (
    User,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUser:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Petstore) -> None:
        user = client.user.create()
        assert user is None

    @parametrize
    def test_method_create_with_all_params(self, client: Petstore) -> None:
        user = client.user.create(
            id=10,
            email="john@email.com",
            first_name="John",
            last_name="James",
            password="12345",
            phone="12345",
            username="theUser",
            user_status=1,
        )
        assert user is None

    @parametrize
    def test_raw_response_create(self, client: Petstore) -> None:
        response = client.user.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @parametrize
    def test_streaming_response_create(self, client: Petstore) -> None:
        with client.user.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Petstore) -> None:
        user = client.user.retrieve(
            "string",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Petstore) -> None:
        response = client.user.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Petstore) -> None:
        with client.user.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Petstore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `username` but received ''"):
            client.user.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Petstore) -> None:
        user = client.user.update(
            "string",
        )
        assert user is None

    @parametrize
    def test_method_update_with_all_params(self, client: Petstore) -> None:
        user = client.user.update(
            "string",
            id=10,
            email="john@email.com",
            first_name="John",
            last_name="James",
            password="12345",
            phone="12345",
            username="theUser",
            user_status=1,
        )
        assert user is None

    @parametrize
    def test_raw_response_update(self, client: Petstore) -> None:
        response = client.user.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @parametrize
    def test_streaming_response_update(self, client: Petstore) -> None:
        with client.user.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Petstore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `existing_username` but received ''"):
            client.user.with_raw_response.update(
                "",
                username="",
            )

    @parametrize
    def test_method_delete(self, client: Petstore) -> None:
        user = client.user.delete(
            "string",
        )
        assert user is None

    @parametrize
    def test_raw_response_delete(self, client: Petstore) -> None:
        response = client.user.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @parametrize
    def test_streaming_response_delete(self, client: Petstore) -> None:
        with client.user.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Petstore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `username` but received ''"):
            client.user.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_create_with_list(self, client: Petstore) -> None:
        user = client.user.create_with_list(
            items=[{}, {}, {}],
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_raw_response_create_with_list(self, client: Petstore) -> None:
        response = client.user.with_raw_response.create_with_list(
            items=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_streaming_response_create_with_list(self, client: Petstore) -> None:
        with client.user.with_streaming_response.create_with_list(
            items=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_login(self, client: Petstore) -> None:
        user = client.user.login()
        assert_matches_type(str, user, path=["response"])

    @parametrize
    def test_method_login_with_all_params(self, client: Petstore) -> None:
        user = client.user.login(
            password="string",
            username="string",
        )
        assert_matches_type(str, user, path=["response"])

    @parametrize
    def test_raw_response_login(self, client: Petstore) -> None:
        response = client.user.with_raw_response.login()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(str, user, path=["response"])

    @parametrize
    def test_streaming_response_login(self, client: Petstore) -> None:
        with client.user.with_streaming_response.login() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(str, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_logout(self, client: Petstore) -> None:
        user = client.user.logout()
        assert user is None

    @parametrize
    def test_raw_response_logout(self, client: Petstore) -> None:
        response = client.user.with_raw_response.logout()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @parametrize
    def test_streaming_response_logout(self, client: Petstore) -> None:
        with client.user.with_streaming_response.logout() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True


class TestAsyncUser:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPetstore) -> None:
        user = await async_client.user.create()
        assert user is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPetstore) -> None:
        user = await async_client.user.create(
            id=10,
            email="john@email.com",
            first_name="John",
            last_name="James",
            password="12345",
            phone="12345",
            username="theUser",
            user_status=1,
        )
        assert user is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPetstore) -> None:
        response = await async_client.user.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPetstore) -> None:
        async with async_client.user.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPetstore) -> None:
        user = await async_client.user.retrieve(
            "string",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPetstore) -> None:
        response = await async_client.user.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPetstore) -> None:
        async with async_client.user.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPetstore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `username` but received ''"):
            await async_client.user.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncPetstore) -> None:
        user = await async_client.user.update(
            "string",
        )
        assert user is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPetstore) -> None:
        user = await async_client.user.update(
            "string",
            id=10,
            email="john@email.com",
            first_name="John",
            last_name="James",
            password="12345",
            phone="12345",
            username="theUser",
            user_status=1,
        )
        assert user is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPetstore) -> None:
        response = await async_client.user.with_raw_response.update(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPetstore) -> None:
        async with async_client.user.with_streaming_response.update(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncPetstore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `existing_username` but received ''"):
            await async_client.user.with_raw_response.update(
                "",
                username="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncPetstore) -> None:
        user = await async_client.user.delete(
            "string",
        )
        assert user is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPetstore) -> None:
        response = await async_client.user.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPetstore) -> None:
        async with async_client.user.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPetstore) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `username` but received ''"):
            await async_client.user.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_create_with_list(self, async_client: AsyncPetstore) -> None:
        user = await async_client.user.create_with_list(
            items=[{}, {}, {}],
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_raw_response_create_with_list(self, async_client: AsyncPetstore) -> None:
        response = await async_client.user.with_raw_response.create_with_list(
            items=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_streaming_response_create_with_list(self, async_client: AsyncPetstore) -> None:
        async with async_client.user.with_streaming_response.create_with_list(
            items=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_login(self, async_client: AsyncPetstore) -> None:
        user = await async_client.user.login()
        assert_matches_type(str, user, path=["response"])

    @parametrize
    async def test_method_login_with_all_params(self, async_client: AsyncPetstore) -> None:
        user = await async_client.user.login(
            password="string",
            username="string",
        )
        assert_matches_type(str, user, path=["response"])

    @parametrize
    async def test_raw_response_login(self, async_client: AsyncPetstore) -> None:
        response = await async_client.user.with_raw_response.login()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(str, user, path=["response"])

    @parametrize
    async def test_streaming_response_login(self, async_client: AsyncPetstore) -> None:
        async with async_client.user.with_streaming_response.login() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(str, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_logout(self, async_client: AsyncPetstore) -> None:
        user = await async_client.user.logout()
        assert user is None

    @parametrize
    async def test_raw_response_logout(self, async_client: AsyncPetstore) -> None:
        response = await async_client.user.with_raw_response.logout()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @parametrize
    async def test_streaming_response_logout(self, async_client: AsyncPetstore) -> None:
        async with async_client.user.with_streaming_response.logout() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True
