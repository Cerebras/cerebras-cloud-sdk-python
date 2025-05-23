# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Union, Iterable, Optional, cast

import httpx

from ..types import completion_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import is_given, maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._streaming import Stream, AsyncStream
from .._base_client import make_request_options
from ..types.completion import Completion

__all__ = ["CompletionsResource", "AsyncCompletionsResource"]


class CompletionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompletionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Cerebras/cerebras-cloud-sdk-python-private#accessing-raw-response-data-eg-headers
        """
        return CompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompletionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Cerebras/cerebras-cloud-sdk-python-private#with_streaming_response
        """
        return CompletionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        model: str,
        best_of: Optional[int] | NotGiven = NOT_GIVEN,
        echo: Optional[bool] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        grammar_root: Optional[str] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[object] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        min_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        prompt: Union[str, List[str], Iterable[int], Iterable[Iterable[int]]] | NotGiven = NOT_GIVEN,
        return_raw_tokens: Optional[bool] | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        stop: Union[str, List[str], None] | NotGiven = NOT_GIVEN,
        stream: Optional[bool] | NotGiven = NOT_GIVEN,
        stream_options: Optional[completion_create_params.StreamOptions] | NotGiven = NOT_GIVEN,
        suffix: Optional[str] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        user: Optional[str] | NotGiven = NOT_GIVEN,
        cf_ray: str | NotGiven = NOT_GIVEN,
        x_amz_cf_id: str | NotGiven = NOT_GIVEN,
        x_delay_time: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Completion | Stream[Completion]:
        """
        Completions

        Args:
          best_of: Generates `best_of` completions server-side and returns the "best" (the one with
              the highest log probability per token). Results cannot be streamed. When used
              with `n`, `best_of` controls the number of candidate completions and `n`
              specifies how many to return – `best_of` must be greater than `n`. **Note:**
              Because this parameter generates many completions, it can quickly consume your
              token quota. Use carefully and ensure that you have reasonable settings for
              `max_tokens` and `stop`

          echo: Echo back the prompt in addition to the completion

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          grammar_root: The grammar root used for structured output generation.

          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a JSON object that maps tokens (specified by their token ID in the
              tokenizer) to an associated bias value from -100 to 100. Mathematically, the
              bias is added to the logits generated by the model prior to sampling. The exact
              effect will vary per model, but values between -1 and 1 should decrease or
              increase likelihood of selection; values like -100 or 100 should result in a ban
              or exclusive selection of the relevant token.

          logprobs: Whether to return log probabilities of the output tokens or not. If true,
              returns the log probabilities of each output token returned in the content of
              message.

          max_tokens: The maximum number of tokens that can be generated in the chat completion. The
              total length of input tokens and generated tokens is limited by the model's
              context length.

          min_tokens: The minimum number of tokens to generate for a completion. If not specified or
              set to 0, the model will generate as many tokens as it deems necessary. Setting
              to -1 sets to max sequence length.

          n: How many chat completion choices to generate for each input message. Note that
              you will be charged based on the number of generated tokens across all of the
              choices. Keep n as 1 to minimize costs.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          prompt: The prompt(s) to generate completions for, encoded as a string, array of
              strings, array of tokens, or array of token arrays.

          return_raw_tokens: Return raw tokens instead of text

          seed: If specified, our system will make a best effort to sample deterministically,
              such that repeated requests with the same `seed` and parameters should return
              the same result. Determinism is not guaranteed.

          stop: Up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          suffix: The suffix that comes after a completion of inserted text. (OpenAI feature, not
              supported)

          temperature: What sampling temperature to use, between 0 and 1.5. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic. We generally recommend altering this or `top_p` but
              not both.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered. We
              generally recommend altering this or `temperature` but not both.

          user: A unique identifier representing your end-user, which can help Cerebras to
              monitor and detect abuse.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "CF-RAY": cf_ray,
                    "X-Amz-Cf-Id": x_amz_cf_id,
                    "X-delay-time": str(x_delay_time) if is_given(x_delay_time) else NOT_GIVEN,
                }
            ),
            **(extra_headers or {}),
        }
        return cast(
            Completion,
            self._post(
                "/v1/completions",
                body=maybe_transform(
                    {
                        "model": model,
                        "best_of": best_of,
                        "echo": echo,
                        "frequency_penalty": frequency_penalty,
                        "grammar_root": grammar_root,
                        "logit_bias": logit_bias,
                        "logprobs": logprobs,
                        "max_tokens": max_tokens,
                        "min_tokens": min_tokens,
                        "n": n,
                        "presence_penalty": presence_penalty,
                        "prompt": prompt,
                        "return_raw_tokens": return_raw_tokens,
                        "seed": seed,
                        "stop": stop,
                        "stream": stream,
                        "stream_options": stream_options,
                        "suffix": suffix,
                        "temperature": temperature,
                        "top_p": top_p,
                        "user": user,
                    },
                    completion_create_params.CompletionCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, Completion),  # Union types cannot be passed in as arguments in the type system
                stream=stream or False,
                stream_cls=Stream[Completion],
            ),
        )


class AsyncCompletionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCompletionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Cerebras/cerebras-cloud-sdk-python-private#accessing-raw-response-data-eg-headers
        """
        return AsyncCompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompletionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Cerebras/cerebras-cloud-sdk-python-private#with_streaming_response
        """
        return AsyncCompletionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        model: str,
        best_of: Optional[int] | NotGiven = NOT_GIVEN,
        echo: Optional[bool] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        grammar_root: Optional[str] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[object] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        min_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        prompt: Union[str, List[str], Iterable[int], Iterable[Iterable[int]]] | NotGiven = NOT_GIVEN,
        return_raw_tokens: Optional[bool] | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        stop: Union[str, List[str], None] | NotGiven = NOT_GIVEN,
        stream: Optional[bool] | NotGiven = NOT_GIVEN,
        stream_options: Optional[completion_create_params.StreamOptions] | NotGiven = NOT_GIVEN,
        suffix: Optional[str] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        user: Optional[str] | NotGiven = NOT_GIVEN,
        cf_ray: str | NotGiven = NOT_GIVEN,
        x_amz_cf_id: str | NotGiven = NOT_GIVEN,
        x_delay_time: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Completion | AsyncStream[Completion]:
        """
        Completions

        Args:
          best_of: Generates `best_of` completions server-side and returns the "best" (the one with
              the highest log probability per token). Results cannot be streamed. When used
              with `n`, `best_of` controls the number of candidate completions and `n`
              specifies how many to return – `best_of` must be greater than `n`. **Note:**
              Because this parameter generates many completions, it can quickly consume your
              token quota. Use carefully and ensure that you have reasonable settings for
              `max_tokens` and `stop`

          echo: Echo back the prompt in addition to the completion

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          grammar_root: The grammar root used for structured output generation.

          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a JSON object that maps tokens (specified by their token ID in the
              tokenizer) to an associated bias value from -100 to 100. Mathematically, the
              bias is added to the logits generated by the model prior to sampling. The exact
              effect will vary per model, but values between -1 and 1 should decrease or
              increase likelihood of selection; values like -100 or 100 should result in a ban
              or exclusive selection of the relevant token.

          logprobs: Whether to return log probabilities of the output tokens or not. If true,
              returns the log probabilities of each output token returned in the content of
              message.

          max_tokens: The maximum number of tokens that can be generated in the chat completion. The
              total length of input tokens and generated tokens is limited by the model's
              context length.

          min_tokens: The minimum number of tokens to generate for a completion. If not specified or
              set to 0, the model will generate as many tokens as it deems necessary. Setting
              to -1 sets to max sequence length.

          n: How many chat completion choices to generate for each input message. Note that
              you will be charged based on the number of generated tokens across all of the
              choices. Keep n as 1 to minimize costs.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          prompt: The prompt(s) to generate completions for, encoded as a string, array of
              strings, array of tokens, or array of token arrays.

          return_raw_tokens: Return raw tokens instead of text

          seed: If specified, our system will make a best effort to sample deterministically,
              such that repeated requests with the same `seed` and parameters should return
              the same result. Determinism is not guaranteed.

          stop: Up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          suffix: The suffix that comes after a completion of inserted text. (OpenAI feature, not
              supported)

          temperature: What sampling temperature to use, between 0 and 1.5. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic. We generally recommend altering this or `top_p` but
              not both.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered. We
              generally recommend altering this or `temperature` but not both.

          user: A unique identifier representing your end-user, which can help Cerebras to
              monitor and detect abuse.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "CF-RAY": cf_ray,
                    "X-Amz-Cf-Id": x_amz_cf_id,
                    "X-delay-time": str(x_delay_time) if is_given(x_delay_time) else NOT_GIVEN,
                }
            ),
            **(extra_headers or {}),
        }
        return cast(
            Completion,
            await self._post(
                "/v1/completions",
                body=await async_maybe_transform(
                    {
                        "model": model,
                        "best_of": best_of,
                        "echo": echo,
                        "frequency_penalty": frequency_penalty,
                        "grammar_root": grammar_root,
                        "logit_bias": logit_bias,
                        "logprobs": logprobs,
                        "max_tokens": max_tokens,
                        "min_tokens": min_tokens,
                        "n": n,
                        "presence_penalty": presence_penalty,
                        "prompt": prompt,
                        "return_raw_tokens": return_raw_tokens,
                        "seed": seed,
                        "stop": stop,
                        "stream": stream,
                        "stream_options": stream_options,
                        "suffix": suffix,
                        "temperature": temperature,
                        "top_p": top_p,
                        "user": user,
                    },
                    completion_create_params.CompletionCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, Completion),  # Union types cannot be passed in as arguments in the type system
                stream=stream or False,
                stream_cls=AsyncStream[Completion],
            ),
        )


class CompletionsResourceWithRawResponse:
    def __init__(self, completions: CompletionsResource) -> None:
        self._completions = completions

        self.create = to_raw_response_wrapper(
            completions.create,
        )


class AsyncCompletionsResourceWithRawResponse:
    def __init__(self, completions: AsyncCompletionsResource) -> None:
        self._completions = completions

        self.create = async_to_raw_response_wrapper(
            completions.create,
        )


class CompletionsResourceWithStreamingResponse:
    def __init__(self, completions: CompletionsResource) -> None:
        self._completions = completions

        self.create = to_streamed_response_wrapper(
            completions.create,
        )


class AsyncCompletionsResourceWithStreamingResponse:
    def __init__(self, completions: AsyncCompletionsResource) -> None:
        self._completions = completions

        self.create = async_to_streamed_response_wrapper(
            completions.create,
        )
