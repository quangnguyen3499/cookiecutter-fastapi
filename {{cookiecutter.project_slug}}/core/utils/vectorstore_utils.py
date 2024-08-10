import os
from typing import Any
from typing import Union

from chromadb import PersistentClient
from core.loggers.app_logging import logger
from langchain_community.vectorstores.chroma import Chroma
from typing_extensions import LiteralString


def load_chroma_vector_store(
    path: Union[str, LiteralString, bytes],
    embedding_function,
    settings: Any,
    collection_name: str,
    tags: str,
) -> Chroma:
    """
    Loads a vector store from disk or initializes an empty one if not found.
    :param path: Base directory path.
    :param settings: Settings for the vector store.
    :param embedding_function: Embedding function for the vector store.
    :param collection_name: Collection name for the vector store.
    :param tags: The tag of the vector store
    :return: Loaded or initialized vector store.
    """
    if os.path.exists(path):
        persistent_client = PersistentClient(path=path, settings=settings)
        vector_store = Chroma(
            client=persistent_client,
            embedding_function=embedding_function,
            collection_name=collection_name,
            collection_metadata={"hnsw:space": "cosine"},
        )
        logger.info(f"# {tags} Documents: {vector_store._collection.count()}")
    else:
        logger.error(f"No vector store found at {path}. Using empty vector store.")
        vector_store = Chroma.from_texts([""], embedding_function)

    return vector_store
