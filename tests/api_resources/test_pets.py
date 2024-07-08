# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from cerebras_minus_cloud import Petstore, AsyncPetstore
from cerebras_minus_cloud.types import (
    Pet,
    APIResponse,
    PetFindByTagsResponse,
    PetFindByStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Petstore) -> None:
        pet = client.pets.create(
            name="doggie",
            photo_urls=["string", "string", "string"],
        )
        assert_matches_type(Pet, pet, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Petstore) -> None:
        pet = client.pets.create(
            name="doggie",
            photo_urls=["string", "string", "string"],
            id=10,
            category={
                "id": 1,
                "name": "Dogs",
            },
            status="available",
            tags=[
                {
                    "id": 0,
                    "name": "string",
                },
                {
                    "id": 0,
                    "name": "string",
                },
                {
                    "id": 0,
                    "name": "string",
                },
            ],
        )
        assert_matches_type(Pet, pet, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Petstore) -> None:
        response = client.pets.with_raw_response.create(
            name="doggie",
            photo_urls=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = response.parse()
        assert_matches_type(Pet, pet, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Petstore) -> None:
        with client.pets.with_streaming_response.create(
            name="doggie",
            photo_urls=["string", "string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = response.parse()
            assert_matches_type(Pet, pet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Petstore) -> None:
        pet = client.pets.retrieve(
            0,
        )
        assert_matches_type(Pet, pet, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Petstore) -> None:
        response = client.pets.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = response.parse()
        assert_matches_type(Pet, pet, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Petstore) -> None:
        with client.pets.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = response.parse()
            assert_matches_type(Pet, pet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Petstore) -> None:
        pet = client.pets.update(
            name="doggie",
            photo_urls=["string", "string", "string"],
        )
        assert_matches_type(Pet, pet, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Petstore) -> None:
        pet = client.pets.update(
            name="doggie",
            photo_urls=["string", "string", "string"],
            id=10,
            category={
                "id": 1,
                "name": "Dogs",
            },
            status="available",
            tags=[
                {
                    "id": 0,
                    "name": "string",
                },
                {
                    "id": 0,
                    "name": "string",
                },
                {
                    "id": 0,
                    "name": "string",
                },
            ],
        )
        assert_matches_type(Pet, pet, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Petstore) -> None:
        response = client.pets.with_raw_response.update(
            name="doggie",
            photo_urls=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = response.parse()
        assert_matches_type(Pet, pet, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Petstore) -> None:
        with client.pets.with_streaming_response.update(
            name="doggie",
            photo_urls=["string", "string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = response.parse()
            assert_matches_type(Pet, pet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Petstore) -> None:
        pet = client.pets.delete(
            0,
        )
        assert pet is None

    @parametrize
    def test_raw_response_delete(self, client: Petstore) -> None:
        response = client.pets.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = response.parse()
        assert pet is None

    @parametrize
    def test_streaming_response_delete(self, client: Petstore) -> None:
        with client.pets.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = response.parse()
            assert pet is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_find_by_status(self, client: Petstore) -> None:
        pet = client.pets.find_by_status()
        assert_matches_type(PetFindByStatusResponse, pet, path=["response"])

    @parametrize
    def test_method_find_by_status_with_all_params(self, client: Petstore) -> None:
        pet = client.pets.find_by_status(
            status="available",
        )
        assert_matches_type(PetFindByStatusResponse, pet, path=["response"])

    @parametrize
    def test_raw_response_find_by_status(self, client: Petstore) -> None:
        response = client.pets.with_raw_response.find_by_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = response.parse()
        assert_matches_type(PetFindByStatusResponse, pet, path=["response"])

    @parametrize
    def test_streaming_response_find_by_status(self, client: Petstore) -> None:
        with client.pets.with_streaming_response.find_by_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = response.parse()
            assert_matches_type(PetFindByStatusResponse, pet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_find_by_tags(self, client: Petstore) -> None:
        pet = client.pets.find_by_tags()
        assert_matches_type(PetFindByTagsResponse, pet, path=["response"])

    @parametrize
    def test_method_find_by_tags_with_all_params(self, client: Petstore) -> None:
        pet = client.pets.find_by_tags(
            tags=["string", "string", "string"],
        )
        assert_matches_type(PetFindByTagsResponse, pet, path=["response"])

    @parametrize
    def test_raw_response_find_by_tags(self, client: Petstore) -> None:
        response = client.pets.with_raw_response.find_by_tags()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = response.parse()
        assert_matches_type(PetFindByTagsResponse, pet, path=["response"])

    @parametrize
    def test_streaming_response_find_by_tags(self, client: Petstore) -> None:
        with client.pets.with_streaming_response.find_by_tags() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = response.parse()
            assert_matches_type(PetFindByTagsResponse, pet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_by_id(self, client: Petstore) -> None:
        pet = client.pets.update_by_id(
            0,
        )
        assert pet is None

    @parametrize
    def test_method_update_by_id_with_all_params(self, client: Petstore) -> None:
        pet = client.pets.update_by_id(
            0,
            name="string",
            status="string",
        )
        assert pet is None

    @parametrize
    def test_raw_response_update_by_id(self, client: Petstore) -> None:
        response = client.pets.with_raw_response.update_by_id(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = response.parse()
        assert pet is None

    @parametrize
    def test_streaming_response_update_by_id(self, client: Petstore) -> None:
        with client.pets.with_streaming_response.update_by_id(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = response.parse()
            assert pet is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_upload_image(self, client: Petstore) -> None:
        pet = client.pets.upload_image(
            0,
            image=b"raw file contents",
        )
        assert_matches_type(APIResponse, pet, path=["response"])

    @parametrize
    def test_method_upload_image_with_all_params(self, client: Petstore) -> None:
        pet = client.pets.upload_image(
            0,
            image=b"raw file contents",
            additional_metadata="string",
        )
        assert_matches_type(APIResponse, pet, path=["response"])

    @parametrize
    def test_raw_response_upload_image(self, client: Petstore) -> None:
        response = client.pets.with_raw_response.upload_image(
            0,
            image=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = response.parse()
        assert_matches_type(APIResponse, pet, path=["response"])

    @parametrize
    def test_streaming_response_upload_image(self, client: Petstore) -> None:
        with client.pets.with_streaming_response.upload_image(
            0,
            image=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = response.parse()
            assert_matches_type(APIResponse, pet, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPetstore) -> None:
        pet = await async_client.pets.create(
            name="doggie",
            photo_urls=["string", "string", "string"],
        )
        assert_matches_type(Pet, pet, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPetstore) -> None:
        pet = await async_client.pets.create(
            name="doggie",
            photo_urls=["string", "string", "string"],
            id=10,
            category={
                "id": 1,
                "name": "Dogs",
            },
            status="available",
            tags=[
                {
                    "id": 0,
                    "name": "string",
                },
                {
                    "id": 0,
                    "name": "string",
                },
                {
                    "id": 0,
                    "name": "string",
                },
            ],
        )
        assert_matches_type(Pet, pet, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPetstore) -> None:
        response = await async_client.pets.with_raw_response.create(
            name="doggie",
            photo_urls=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = await response.parse()
        assert_matches_type(Pet, pet, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPetstore) -> None:
        async with async_client.pets.with_streaming_response.create(
            name="doggie",
            photo_urls=["string", "string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = await response.parse()
            assert_matches_type(Pet, pet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPetstore) -> None:
        pet = await async_client.pets.retrieve(
            0,
        )
        assert_matches_type(Pet, pet, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPetstore) -> None:
        response = await async_client.pets.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = await response.parse()
        assert_matches_type(Pet, pet, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPetstore) -> None:
        async with async_client.pets.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = await response.parse()
            assert_matches_type(Pet, pet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncPetstore) -> None:
        pet = await async_client.pets.update(
            name="doggie",
            photo_urls=["string", "string", "string"],
        )
        assert_matches_type(Pet, pet, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPetstore) -> None:
        pet = await async_client.pets.update(
            name="doggie",
            photo_urls=["string", "string", "string"],
            id=10,
            category={
                "id": 1,
                "name": "Dogs",
            },
            status="available",
            tags=[
                {
                    "id": 0,
                    "name": "string",
                },
                {
                    "id": 0,
                    "name": "string",
                },
                {
                    "id": 0,
                    "name": "string",
                },
            ],
        )
        assert_matches_type(Pet, pet, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPetstore) -> None:
        response = await async_client.pets.with_raw_response.update(
            name="doggie",
            photo_urls=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = await response.parse()
        assert_matches_type(Pet, pet, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPetstore) -> None:
        async with async_client.pets.with_streaming_response.update(
            name="doggie",
            photo_urls=["string", "string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = await response.parse()
            assert_matches_type(Pet, pet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncPetstore) -> None:
        pet = await async_client.pets.delete(
            0,
        )
        assert pet is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPetstore) -> None:
        response = await async_client.pets.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = await response.parse()
        assert pet is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPetstore) -> None:
        async with async_client.pets.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = await response.parse()
            assert pet is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_find_by_status(self, async_client: AsyncPetstore) -> None:
        pet = await async_client.pets.find_by_status()
        assert_matches_type(PetFindByStatusResponse, pet, path=["response"])

    @parametrize
    async def test_method_find_by_status_with_all_params(self, async_client: AsyncPetstore) -> None:
        pet = await async_client.pets.find_by_status(
            status="available",
        )
        assert_matches_type(PetFindByStatusResponse, pet, path=["response"])

    @parametrize
    async def test_raw_response_find_by_status(self, async_client: AsyncPetstore) -> None:
        response = await async_client.pets.with_raw_response.find_by_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = await response.parse()
        assert_matches_type(PetFindByStatusResponse, pet, path=["response"])

    @parametrize
    async def test_streaming_response_find_by_status(self, async_client: AsyncPetstore) -> None:
        async with async_client.pets.with_streaming_response.find_by_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = await response.parse()
            assert_matches_type(PetFindByStatusResponse, pet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_find_by_tags(self, async_client: AsyncPetstore) -> None:
        pet = await async_client.pets.find_by_tags()
        assert_matches_type(PetFindByTagsResponse, pet, path=["response"])

    @parametrize
    async def test_method_find_by_tags_with_all_params(self, async_client: AsyncPetstore) -> None:
        pet = await async_client.pets.find_by_tags(
            tags=["string", "string", "string"],
        )
        assert_matches_type(PetFindByTagsResponse, pet, path=["response"])

    @parametrize
    async def test_raw_response_find_by_tags(self, async_client: AsyncPetstore) -> None:
        response = await async_client.pets.with_raw_response.find_by_tags()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = await response.parse()
        assert_matches_type(PetFindByTagsResponse, pet, path=["response"])

    @parametrize
    async def test_streaming_response_find_by_tags(self, async_client: AsyncPetstore) -> None:
        async with async_client.pets.with_streaming_response.find_by_tags() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = await response.parse()
            assert_matches_type(PetFindByTagsResponse, pet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_by_id(self, async_client: AsyncPetstore) -> None:
        pet = await async_client.pets.update_by_id(
            0,
        )
        assert pet is None

    @parametrize
    async def test_method_update_by_id_with_all_params(self, async_client: AsyncPetstore) -> None:
        pet = await async_client.pets.update_by_id(
            0,
            name="string",
            status="string",
        )
        assert pet is None

    @parametrize
    async def test_raw_response_update_by_id(self, async_client: AsyncPetstore) -> None:
        response = await async_client.pets.with_raw_response.update_by_id(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = await response.parse()
        assert pet is None

    @parametrize
    async def test_streaming_response_update_by_id(self, async_client: AsyncPetstore) -> None:
        async with async_client.pets.with_streaming_response.update_by_id(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = await response.parse()
            assert pet is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_upload_image(self, async_client: AsyncPetstore) -> None:
        pet = await async_client.pets.upload_image(
            0,
            image=b"raw file contents",
        )
        assert_matches_type(APIResponse, pet, path=["response"])

    @parametrize
    async def test_method_upload_image_with_all_params(self, async_client: AsyncPetstore) -> None:
        pet = await async_client.pets.upload_image(
            0,
            image=b"raw file contents",
            additional_metadata="string",
        )
        assert_matches_type(APIResponse, pet, path=["response"])

    @parametrize
    async def test_raw_response_upload_image(self, async_client: AsyncPetstore) -> None:
        response = await async_client.pets.with_raw_response.upload_image(
            0,
            image=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pet = await response.parse()
        assert_matches_type(APIResponse, pet, path=["response"])

    @parametrize
    async def test_streaming_response_upload_image(self, async_client: AsyncPetstore) -> None:
        async with async_client.pets.with_streaming_response.upload_image(
            0,
            image=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pet = await response.parse()
            assert_matches_type(APIResponse, pet, path=["response"])

        assert cast(Any, response.is_closed) is True
