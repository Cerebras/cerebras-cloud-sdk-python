# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "ModelListResponse",
    "ModelMetadataList",
    "ModelMetadataListData",
    "OpenRouterModelsResponse",
    "OpenRouterModelsResponseData",
    "OpenRouterModelsResponseDataPricing",
    "OpenRouterModelsResponseDataDatacenter",
    "OpenRouterModelsResponseDataOpenrouter",
    "HuggingFaceModelsResponse",
    "HuggingFaceModelsResponseData",
    "HuggingFaceModelsResponseDataPricing",
    "HuggingFaceModelsResponseDataCapabilities",
]


class ModelMetadataListData(BaseModel):
    id: str

    created: Optional[int] = None

    object: Optional[Literal["model"]] = None

    owned_by: Optional[str] = None


class ModelMetadataList(BaseModel):
    data: List[ModelMetadataListData]

    object: Optional[Literal["list"]] = None


class OpenRouterModelsResponseDataPricing(BaseModel):
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


class OpenRouterModelsResponseDataDatacenter(BaseModel):
    """Datacenter location information."""

    country_code: str
    """ISO 3166 Alpha-2 country code"""


class OpenRouterModelsResponseDataOpenrouter(BaseModel):
    """OpenRouter metadata."""

    slug: str
    """OpenRouter slug for the model"""


class OpenRouterModelsResponseData(BaseModel):
    """Model in OpenRouter-compatible format."""

    id: str
    """Model ID with provider prefix, e.g., 'cerebras/llama3.1-8b'"""

    context_length: int

    created: int
    """Unix timestamp when model was created"""

    max_output_length: int
    """Maximum number of output tokens"""

    name: str

    pricing: OpenRouterModelsResponseDataPricing
    """OpenRouter pricing format."""

    datacenters: Optional[List[OpenRouterModelsResponseDataDatacenter]] = None
    """Datacenter locations"""

    description: Optional[str] = None
    """Model description"""

    hugging_face_id: Optional[str] = None
    """The corresponding HuggingFace Hub model ID, if available"""

    input_modalities: Optional[List[str]] = None
    """Supported input modalities (text, image, file)"""

    openrouter: Optional[OpenRouterModelsResponseDataOpenrouter] = None
    """OpenRouter metadata."""

    output_modalities: Optional[List[str]] = None
    """Supported output modalities (text, image, file)"""

    quantization: Optional[str] = None
    """Model quantization (fp16 only for Cerebras)"""

    supported_features: Optional[List[str]] = None
    """List of supported features"""

    supported_sampling_parameters: Optional[List[str]] = None
    """List of supported sampling parameters"""


class OpenRouterModelsResponse(BaseModel):
    """OpenRouter-compatible list of models."""

    data: List[OpenRouterModelsResponseData]


class HuggingFaceModelsResponseDataPricing(BaseModel):
    """HuggingFace pricing format - price in USD per million tokens."""

    input: float
    """Price in USD per million input tokens"""

    output: float
    """Price in USD per million output tokens"""


class HuggingFaceModelsResponseDataCapabilities(BaseModel):
    """HuggingFace capabilities format."""

    function_calling: Optional[bool] = None

    streaming: Optional[bool] = None

    structured_outputs: Optional[bool] = None

    vision: Optional[bool] = None


class HuggingFaceModelsResponseData(BaseModel):
    """Model in HuggingFace-compatible format for inference providers.

    This format is used by HuggingFace to power their provider comparison table
    and provider selection features.
    """

    id: str

    context_length: int
    """Supported context length in tokens"""

    created: int

    owned_by: str

    pricing: HuggingFaceModelsResponseDataPricing
    """HuggingFace pricing format - price in USD per million tokens."""

    capabilities: Optional[HuggingFaceModelsResponseDataCapabilities] = None
    """HuggingFace capabilities format."""

    hugging_face_id: Optional[str] = None
    """The corresponding HuggingFace Hub model ID"""

    object: Optional[Literal["model"]] = None


class HuggingFaceModelsResponse(BaseModel):
    """HuggingFace-compatible list of models."""

    data: List[HuggingFaceModelsResponseData]

    object: Optional[Literal["list"]] = None


ModelListResponse: TypeAlias = Union[ModelMetadataList, OpenRouterModelsResponse, HuggingFaceModelsResponse]
