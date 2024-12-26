from farm_haystack.nodes.retriever.base import BaseRetriever
from farm_haystack.nodes.retriever.dense import (
    DensePassageRetriever,
    DenseRetriever,
    EmbeddingRetriever,
    MultihopEmbeddingRetriever,
    TableTextRetriever,
)
from farm_haystack.nodes.retriever.multimodal import MultiModalRetriever
from farm_haystack.nodes.retriever.sparse import BM25Retriever, FilterRetriever, TfidfRetriever
from farm_haystack.nodes.retriever.link_content import LinkContentFetcher
from farm_haystack.nodes.retriever.web import WebRetriever
