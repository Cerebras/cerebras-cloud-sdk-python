# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal

import httpx

from ..types import (
    pet_create_params,
    pet_update_params,
    pet_find_by_tags_params,
    pet_update_by_id_params,
    pet_upload_image_params,
    pet_find_by_status_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven, FileTypes
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..types.pet import Pet
from .._base_client import (
    make_request_options,
)
from ..types.api_response import APIResponse
from ..types.pet_find_by_tags_response import PetFindByTagsResponse
from ..types.pet_find_by_status_response import PetFindByStatusResponse

__all__ = ["PetsResource", "AsyncPetsResource"]


class PetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PetsResourceWithRawResponse:
        return PetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PetsResourceWithStreamingResponse:
        return PetsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        photo_urls: List[str],
        id: int | NotGiven = NOT_GIVEN,
        category: pet_create_params.Category | NotGiven = NOT_GIVEN,
        status: Literal["available", "pending", "sold"] | NotGiven = NOT_GIVEN,
        tags: Iterable[pet_create_params.Tag] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Pet:
        """
        Add a new pet to the store

        Args:
          status: pet status in the store

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/pet",
            body=maybe_transform(
                {
                    "name": name,
                    "photo_urls": photo_urls,
                    "id": id,
                    "category": category,
                    "status": status,
                    "tags": tags,
                },
                pet_create_params.PetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Pet,
        )

    def retrieve(
        self,
        pet_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Pet:
        """
        Returns a single pet

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/pet/{pet_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Pet,
        )

    def update(
        self,
        *,
        name: str,
        photo_urls: List[str],
        id: int | NotGiven = NOT_GIVEN,
        category: pet_update_params.Category | NotGiven = NOT_GIVEN,
        status: Literal["available", "pending", "sold"] | NotGiven = NOT_GIVEN,
        tags: Iterable[pet_update_params.Tag] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Pet:
        """
        Update an existing pet by Id

        Args:
          status: pet status in the store

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/pet",
            body=maybe_transform(
                {
                    "name": name,
                    "photo_urls": photo_urls,
                    "id": id,
                    "category": category,
                    "status": status,
                    "tags": tags,
                },
                pet_update_params.PetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Pet,
        )

    def delete(
        self,
        pet_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        delete a pet

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/pet/{pet_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def find_by_status(
        self,
        *,
        status: Literal["available", "pending", "sold"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PetFindByStatusResponse:
        """
        Multiple status values can be provided with comma separated strings

        Args:
          status: Status values that need to be considered for filter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/pet/findByStatus",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"status": status}, pet_find_by_status_params.PetFindByStatusParams),
            ),
            cast_to=PetFindByStatusResponse,
        )

    def find_by_tags(
        self,
        *,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PetFindByTagsResponse:
        """Multiple tags can be provided with comma separated strings.

        Use tag1, tag2, tag3
        for testing.

        Args:
          tags: Tags to filter by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/pet/findByTags",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"tags": tags}, pet_find_by_tags_params.PetFindByTagsParams),
            ),
            cast_to=PetFindByTagsResponse,
        )

    def update_by_id(
        self,
        pet_id: int,
        *,
        name: str | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Updates a pet in the store with form data

        Args:
          name: Name of pet that needs to be updated

          status: Status of pet that needs to be updated

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/pet/{pet_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name": name,
                        "status": status,
                    },
                    pet_update_by_id_params.PetUpdateByIDParams,
                ),
            ),
            cast_to=NoneType,
        )

    def upload_image(
        self,
        pet_id: int,
        *,
        image: FileTypes,
        additional_metadata: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIResponse:
        """
        uploads an image

        Args:
          additional_metadata: Additional Metadata

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/pet/{pet_id}/uploadImage",
            body=maybe_transform(image, pet_upload_image_params.PetUploadImageParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"additional_metadata": additional_metadata}, pet_upload_image_params.PetUploadImageParams
                ),
            ),
            cast_to=APIResponse,
        )


class AsyncPetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPetsResourceWithRawResponse:
        return AsyncPetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPetsResourceWithStreamingResponse:
        return AsyncPetsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        photo_urls: List[str],
        id: int | NotGiven = NOT_GIVEN,
        category: pet_create_params.Category | NotGiven = NOT_GIVEN,
        status: Literal["available", "pending", "sold"] | NotGiven = NOT_GIVEN,
        tags: Iterable[pet_create_params.Tag] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Pet:
        """
        Add a new pet to the store

        Args:
          status: pet status in the store

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/pet",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "photo_urls": photo_urls,
                    "id": id,
                    "category": category,
                    "status": status,
                    "tags": tags,
                },
                pet_create_params.PetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Pet,
        )

    async def retrieve(
        self,
        pet_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Pet:
        """
        Returns a single pet

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/pet/{pet_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Pet,
        )

    async def update(
        self,
        *,
        name: str,
        photo_urls: List[str],
        id: int | NotGiven = NOT_GIVEN,
        category: pet_update_params.Category | NotGiven = NOT_GIVEN,
        status: Literal["available", "pending", "sold"] | NotGiven = NOT_GIVEN,
        tags: Iterable[pet_update_params.Tag] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Pet:
        """
        Update an existing pet by Id

        Args:
          status: pet status in the store

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/pet",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "photo_urls": photo_urls,
                    "id": id,
                    "category": category,
                    "status": status,
                    "tags": tags,
                },
                pet_update_params.PetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Pet,
        )

    async def delete(
        self,
        pet_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        delete a pet

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/pet/{pet_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def find_by_status(
        self,
        *,
        status: Literal["available", "pending", "sold"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PetFindByStatusResponse:
        """
        Multiple status values can be provided with comma separated strings

        Args:
          status: Status values that need to be considered for filter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/pet/findByStatus",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"status": status}, pet_find_by_status_params.PetFindByStatusParams),
            ),
            cast_to=PetFindByStatusResponse,
        )

    async def find_by_tags(
        self,
        *,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PetFindByTagsResponse:
        """Multiple tags can be provided with comma separated strings.

        Use tag1, tag2, tag3
        for testing.

        Args:
          tags: Tags to filter by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/pet/findByTags",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"tags": tags}, pet_find_by_tags_params.PetFindByTagsParams),
            ),
            cast_to=PetFindByTagsResponse,
        )

    async def update_by_id(
        self,
        pet_id: int,
        *,
        name: str | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Updates a pet in the store with form data

        Args:
          name: Name of pet that needs to be updated

          status: Status of pet that needs to be updated

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/pet/{pet_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "name": name,
                        "status": status,
                    },
                    pet_update_by_id_params.PetUpdateByIDParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def upload_image(
        self,
        pet_id: int,
        *,
        image: FileTypes,
        additional_metadata: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIResponse:
        """
        uploads an image

        Args:
          additional_metadata: Additional Metadata

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/pet/{pet_id}/uploadImage",
            body=await async_maybe_transform(image, pet_upload_image_params.PetUploadImageParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"additional_metadata": additional_metadata}, pet_upload_image_params.PetUploadImageParams
                ),
            ),
            cast_to=APIResponse,
        )


class PetsResourceWithRawResponse:
    def __init__(self, pets: PetsResource) -> None:
        self._pets = pets

        self.create = to_raw_response_wrapper(
            pets.create,
        )
        self.retrieve = to_raw_response_wrapper(
            pets.retrieve,
        )
        self.update = to_raw_response_wrapper(
            pets.update,
        )
        self.delete = to_raw_response_wrapper(
            pets.delete,
        )
        self.find_by_status = to_raw_response_wrapper(
            pets.find_by_status,
        )
        self.find_by_tags = to_raw_response_wrapper(
            pets.find_by_tags,
        )
        self.update_by_id = to_raw_response_wrapper(
            pets.update_by_id,
        )
        self.upload_image = to_raw_response_wrapper(
            pets.upload_image,
        )


class AsyncPetsResourceWithRawResponse:
    def __init__(self, pets: AsyncPetsResource) -> None:
        self._pets = pets

        self.create = async_to_raw_response_wrapper(
            pets.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            pets.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            pets.update,
        )
        self.delete = async_to_raw_response_wrapper(
            pets.delete,
        )
        self.find_by_status = async_to_raw_response_wrapper(
            pets.find_by_status,
        )
        self.find_by_tags = async_to_raw_response_wrapper(
            pets.find_by_tags,
        )
        self.update_by_id = async_to_raw_response_wrapper(
            pets.update_by_id,
        )
        self.upload_image = async_to_raw_response_wrapper(
            pets.upload_image,
        )


class PetsResourceWithStreamingResponse:
    def __init__(self, pets: PetsResource) -> None:
        self._pets = pets

        self.create = to_streamed_response_wrapper(
            pets.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            pets.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            pets.update,
        )
        self.delete = to_streamed_response_wrapper(
            pets.delete,
        )
        self.find_by_status = to_streamed_response_wrapper(
            pets.find_by_status,
        )
        self.find_by_tags = to_streamed_response_wrapper(
            pets.find_by_tags,
        )
        self.update_by_id = to_streamed_response_wrapper(
            pets.update_by_id,
        )
        self.upload_image = to_streamed_response_wrapper(
            pets.upload_image,
        )


class AsyncPetsResourceWithStreamingResponse:
    def __init__(self, pets: AsyncPetsResource) -> None:
        self._pets = pets

        self.create = async_to_streamed_response_wrapper(
            pets.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            pets.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            pets.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            pets.delete,
        )
        self.find_by_status = async_to_streamed_response_wrapper(
            pets.find_by_status,
        )
        self.find_by_tags = async_to_streamed_response_wrapper(
            pets.find_by_tags,
        )
        self.update_by_id = async_to_streamed_response_wrapper(
            pets.update_by_id,
        )
        self.upload_image = async_to_streamed_response_wrapper(
            pets.upload_image,
        )
