from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `cerebras.cloud.sdk.resources` module.

    This is used so that we can lazily import `cerebras.cloud.sdk.resources` only when
    needed *and* so that users can just import `cerebras.cloud.sdk` and reference `cerebras.cloud.sdk.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("cerebras.cloud.sdk.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
