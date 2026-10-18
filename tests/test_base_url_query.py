from __future__ import annotations

import httpx
import pytest

from cerebras.cloud.sdk import Cerebras, AsyncCerebras

BASE_URLS = ["https://proxy.example", "https://proxy.example/api/", "https://proxy.example/tenant%2Fname"]


@pytest.mark.parametrize("base_url", BASE_URLS)
@pytest.mark.parametrize("query", ["", "?route=base&tag=a%2Fb"])
@pytest.mark.parametrize("override", [False, True])
def test_models_list_with_base_url_query(base_url: str, query: str, override: bool) -> None:
    seen: list[httpx.Request] = []

    def handle(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={"data": [], "object": "list"})

    extra = {"route": "request"} if override else {}
    with httpx.Client(transport=httpx.MockTransport(handle)) as transport:
        with Cerebras(
            api_key="test-key", warm_tcp_connection=False, base_url=base_url + query, http_client=transport
        ) as client:
            client.models.list(format="default", extra_query=extra)

    expected_path = httpx.URL(base_url).raw_path.rstrip(b"/") + b"/v1/models"
    assert seen[0].url.copy_with(query=None).raw_path == expected_path
    assert dict(seen[0].url.params) == {**dict(httpx.URL(base_url + query).params), "format": "default", **extra}
    assert seen[0].headers["authorization"] == "Bearer test-key"


@pytest.mark.parametrize("base_url", BASE_URLS)
@pytest.mark.parametrize("query", ["", "?route=base&tag=a%2Fb"])
@pytest.mark.parametrize("override", [False, True])
async def test_async_models_list_with_base_url_query(base_url: str, query: str, override: bool) -> None:
    seen: list[httpx.Request] = []

    def handle(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={"data": [], "object": "list"})

    extra = {"route": "request"} if override else {}
    async with httpx.AsyncClient(transport=httpx.MockTransport(handle)) as transport:
        async with AsyncCerebras(
            api_key="test-key", warm_tcp_connection=False, base_url=base_url + query, http_client=transport
        ) as client:
            await client.models.list(format="default", extra_query=extra)

    expected_path = httpx.URL(base_url).raw_path.rstrip(b"/") + b"/v1/models"
    assert seen[0].url.copy_with(query=None).raw_path == expected_path
    assert dict(seen[0].url.params) == {**dict(httpx.URL(base_url + query).params), "format": "default", **extra}
    assert seen[0].headers["authorization"] == "Bearer test-key"
