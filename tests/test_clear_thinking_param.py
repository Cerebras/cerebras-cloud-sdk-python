from __future__ import annotations

import os
import json

import httpx
import pytest
from respx import MockRouter

from cerebras.cloud.sdk import Cerebras, AsyncCerebras

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClearThinking:
    @pytest.mark.respx(base_url=base_url)
    def test_clear_thinking_is_sent_in_body(self, respx_mock: MockRouter, client: Cerebras) -> None:
        def handler(request: httpx.Request) -> httpx.Response:
            body = json.loads((request.content or b"{}").decode())
            assert body.get("clear_thinking") is True
            return httpx.Response(200, json={"error": {"message": "ok"}, "status_code": 200})

        respx_mock.post("/v1/chat/completions").mock(side_effect=handler)

        # This should not be blocked by the SDK and should be serialized into the request body.
        client.chat.completions.create(model="model", clear_thinking=True)

    @pytest.mark.respx(base_url=base_url)
    async def test_clear_thinking_is_sent_in_body_async(
        self, respx_mock: MockRouter, async_client: AsyncCerebras
    ) -> None:
        def handler(request: httpx.Request) -> httpx.Response:
            body = json.loads((request.content or b"{}").decode())
            assert body.get("clear_thinking") is True
            return httpx.Response(200, json={"error": {"message": "ok"}, "status_code": 200})

        respx_mock.post("/v1/chat/completions").mock(side_effect=handler)

        await async_client.chat.completions.create(model="model", clear_thinking=True)
