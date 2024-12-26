# pylint: disable=wrong-import-position
# Logging is not configured here on purpose, see https://github.com/deepset-ai/haystack/issues/2485

from importlib import metadata

__version__: str = str(metadata.version("farm-haystack"))


import farm_haystack.silenceable_tqdm  # Needs to be imported first to wrap TQDM for all following modules
from farm_haystack.schema import Document, Answer, Label, MultiLabel, Span, EvaluationResult, TableCell
from farm_haystack.nodes.base import BaseComponent
from farm_haystack.pipelines.base import Pipeline
from farm_haystack.environment import set_pytorch_secure_model_loading
from farm_haystack.mmh3 import hash128


# Enables torch's secure model loading through setting an env var.
# Does not use torch.
set_pytorch_secure_model_loading()
