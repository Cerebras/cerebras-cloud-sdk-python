# Chat

## Completions

Types:

```python
from cerebras.cloud.sdk.types.chat import ChatCompletion, CompletionCreateResponse
```

Methods:

- <code title="post /v1/chat/completions">client.chat.completions.<a href="./src/cerebras/cloud/sdk/resources/chat/completions.py">create</a>(\*\*<a href="src/cerebras/cloud/sdk/types/chat/completion_create_params.py">params</a>) -> <a href="./src/cerebras/cloud/sdk/types/chat/completion_create_response.py">CompletionCreateResponse</a></code>

# Models

Types:

```python
from cerebras.cloud.sdk.types import ModelRetrieveResponse, ModelListResponse
```

Methods:

- <code title="get /v1/models/{model_id}">client.models.<a href="./src/cerebras/cloud/sdk/resources/models.py">retrieve</a>(model_id) -> <a href="./src/cerebras/cloud/sdk/types/model_retrieve_response.py">ModelRetrieveResponse</a></code>
- <code title="get /v1/models">client.models.<a href="./src/cerebras/cloud/sdk/resources/models.py">list</a>() -> <a href="./src/cerebras/cloud/sdk/types/model_list_response.py">ModelListResponse</a></code>
