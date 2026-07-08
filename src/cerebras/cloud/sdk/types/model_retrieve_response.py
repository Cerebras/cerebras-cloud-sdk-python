# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "ModelRetrieveResponse",
    "ModelMetadata",
    "OpenRouterModel",
    "OpenRouterModelPricing",
    "OpenRouterModelDatacenter",
    "OpenRouterModelOpenrouter",
    "HuggingFaceModel",
    "HuggingFaceModelPricing",
    "HuggingFaceModelCapabilities",
    "PublicModel",
    "PublicModelArchitecture",
    "PublicModelCapabilities",
    "PublicModelLimits",
    "PublicModelPricing",
    "PublicModelSupportedParameters",
]


class ModelMetadata(BaseModel):
    id: str

    created: Optional[int] = None

    object: Optional[Literal["model"]] = None

    owned_by: Optional[str] = None


class OpenRouterModelPricing(BaseModel):
    """OpenRouter pricing format."""

    completion: str
    """Cost per output token as string"""

    prompt: str
    """Cost per input token as string"""

    image: Optional[str] = None
    """Cost per image as string"""

    input_cache_read: Optional[str] = None
    """Cost per cached input token read as string"""

    input_cache_write: Optional[str] = None
    """Cost per cached input token write as string"""

    request: Optional[str] = None
    """Cost per request as string"""


class OpenRouterModelDatacenter(BaseModel):
    """Datacenter location information."""

    country_code: str
    """ISO 3166 Alpha-2 country code"""


class OpenRouterModelOpenrouter(BaseModel):
    """OpenRouter metadata."""

    slug: str
    """OpenRouter slug for the model"""


class OpenRouterModel(BaseModel):
    """Model in OpenRouter-compatible format."""

    id: str
    """Model ID with provider prefix, e.g., 'cerebras/llama3.1-8b'"""

    context_length: int

    created: int
    """Unix timestamp when model was created"""

    max_output_length: int
    """Maximum number of output tokens"""

    name: str

    pricing: OpenRouterModelPricing
    """OpenRouter pricing format."""

    datacenters: Optional[List[OpenRouterModelDatacenter]] = None
    """Datacenter locations"""

    description: Optional[str] = None
    """Model description"""

    hugging_face_id: Optional[str] = None
    """The corresponding HuggingFace Hub model ID, if available"""

    input_modalities: Optional[List[str]] = None
    """Supported input modalities (text, image, file)"""

    openrouter: Optional[OpenRouterModelOpenrouter] = None
    """OpenRouter metadata."""

    output_modalities: Optional[List[str]] = None
    """Supported output modalities (text, image, file)"""

    quantization: Optional[str] = None
    """Model quantization (fp16 only for Cerebras)"""

    supported_features: Optional[List[str]] = None
    """List of supported features"""

    supported_sampling_parameters: Optional[List[str]] = None
    """List of supported sampling parameters"""


class HuggingFaceModelPricing(BaseModel):
    """HuggingFace pricing format - price in USD per million tokens."""

    input: float
    """Price in USD per million input tokens"""

    output: float
    """Price in USD per million output tokens"""


class HuggingFaceModelCapabilities(BaseModel):
    """HuggingFace capabilities format."""

    function_calling: Optional[bool] = None

    streaming: Optional[bool] = None

    structured_outputs: Optional[bool] = None

    vision: Optional[bool] = None


class HuggingFaceModel(BaseModel):
    """Model in HuggingFace-compatible format for inference providers.

    This format is used by HuggingFace to power their provider comparison table
    and provider selection features.
    """

    id: str

    context_length: int
    """Supported context length in tokens"""

    created: int

    owned_by: str

    pricing: HuggingFaceModelPricing
    """HuggingFace pricing format - price in USD per million tokens."""

    capabilities: Optional[HuggingFaceModelCapabilities] = None
    """HuggingFace capabilities format."""

    hugging_face_id: Optional[str] = None
    """The corresponding HuggingFace Hub model ID"""

    object: Optional[Literal["model"]] = None


class PublicModelArchitecture(BaseModel):
    """Technical architecture details of the model."""

    modality: Literal["text", "text+vision", "multimodal"]
    """The modality of the model (e.g., 'text', 'text+vision', 'multimodal')."""

    tokenizer: str
    """The tokenizer used by the model (e.g., 'Llama3', 'GPT4')."""

    instruct_type: Optional[str] = None
    """The instruction format type used for fine-tuning (e.g., 'llama3', 'chatml')."""


class PublicModelCapabilities(BaseModel):
    """The capabilities supported by the model."""

    function_calling: Optional[bool] = None
    """Indicates if the model supports function calling (tool use)."""

    json_mode: Optional[bool] = None
    """Indicates if the model supports JSON mode (guaranteed JSON output)."""

    parallel_tool_calls: Optional[bool] = None
    """Indicates if the model supports parallel tool calls."""

    reasoning: Optional[bool] = None
    """Indicates if the model supports reasoning/chain-of-thought outputs."""

    response_format: Optional[bool] = None
    """Indicates if the model supports the response_format parameter."""

    streaming: Optional[bool] = None
    """
    Indicates if the model supports streaming responses via Server-Sent Events
    (SSE).
    """

    structured_outputs: Optional[bool] = None
    """Indicates if the model supports structured outputs (e.g.

    JSON schema enforcement).
    """

    tool_choice: Optional[bool] = None
    """Indicates if the model supports the tool_choice parameter."""

    tools: Optional[bool] = None
    """Indicates if the model supports the tools parameter."""

    vision: Optional[bool] = None
    """Indicates if the model accepts image inputs (vision capabilities)."""


class PublicModelLimits(BaseModel):
    """Usage limits and constraints for the model."""

    max_completion_tokens: int
    """The maximum number of tokens that can be generated in a single completion."""

    max_context_length: int
    """The maximum context window size in tokens."""

    requests_per_minute: Optional[int] = None
    """The default rate limit for requests per minute (RPM)."""

    tokens_per_minute: Optional[int] = None
    """The default rate limit for tokens per minute (TPM)."""


class PublicModelPricing(BaseModel):
    """Pricing details for the model."""

    completion: str
    """Cost per token for completion (output) tokens in USD."""

    prompt: str
    """Cost per token for prompt (input) tokens in USD."""


class PublicModelSupportedParameters(BaseModel):
    """Sampling parameters supported by the model."""

    frequency_penalty: Optional[bool] = None
    """Supports frequency_penalty parameter."""

    logit_bias: Optional[bool] = None
    """Supports logit_bias parameter."""

    logprobs: Optional[bool] = None
    """Supports logprobs output."""

    max_completion_tokens: Optional[bool] = None
    """Supports max_completion_tokens parameter."""

    presence_penalty: Optional[bool] = None
    """Supports presence_penalty parameter."""

    repetition_penalty: Optional[bool] = None
    """Supports repetition_penalty parameter."""

    seed: Optional[bool] = None
    """Supports seed for reproducible outputs."""

    stop: Optional[bool] = None
    """Supports stop sequences parameter."""

    temperature: Optional[bool] = None
    """Supports temperature sampling parameter."""

    top_logprobs: Optional[bool] = None
    """Supports top_logprobs parameter."""

    top_p: Optional[bool] = None
    """Supports top_p (nucleus) sampling parameter."""


class PublicModel(BaseModel):
    """
    Complete model specification following OpenAI-compatible schema
    with extensions for OpenRouter/HuggingFace compatibility.
    """

    id: str
    """The unique identifier for the model (e.g., 'llama3.1-8b')."""

    architecture: PublicModelArchitecture
    """Technical architecture details of the model."""

    capabilities: PublicModelCapabilities
    """The capabilities supported by the model."""

    created: int
    """The Unix timestamp (in seconds) when the model was created."""

    description: str
    """A brief description of the model."""

    limits: PublicModelLimits
    """Usage limits and constraints for the model."""

    name: str
    """The human-readable name of the model."""

    owned_by: str
    """The organization that owns or created the model."""

    pricing: PublicModelPricing
    """Pricing details for the model."""

    supported_parameters: PublicModelSupportedParameters
    """Sampling parameters supported by the model."""

    datacenter_locations: Optional[List[str]] = None
    """
    List of datacenter locations where this model is deployed (e.g., ['us-east-1',
    'eu-west-1']).
    """

    deprecated: Optional[bool] = None
    """
    Indicates if the model is deprecated and should not be used for new
    applications.
    """

    hugging_face_id: Optional[str] = None
    """
    The corresponding HuggingFace Hub model ID, if available (e.g.,
    'meta-llama/Llama-3.1-8B-Instruct').
    """

    object: Optional[Literal["model"]] = None
    """The object type, which is always 'model'."""

    preview: Optional[bool] = None
    """Indicates if the model is in preview or beta status."""

    quantization: Optional[str] = None
    """Quantization precision (e.g., 'FP16', 'FP16/FP8 (weights only)')."""


ModelRetrieveResponse: TypeAlias = Union[ModelMetadata, OpenRouterModel, HuggingFaceModel, PublicModel]
