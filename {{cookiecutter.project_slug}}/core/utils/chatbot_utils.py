import os

from configs.common_config import settings
from core.constants import BASE_DIR
from core.constants import CHROMA_DB_DETAILS_PATH
from core.constants import CHROMA_DB_PATH
from core.constants import CHROMA_DEFAULT_SETTINGS
from core.constants import CHROMA_EXAMPLES_PATH
from core.constants import DETAIL_EXPERTS_COLLECTION_NAME
from core.constants import EMBEDDING_3_DIMENSIONS
from core.constants import EXAMPLES_COLLECTION_NAME
from core.constants import EXPERTS_COLLECTION_NAME
from core.constants import SHORTEN_EMBEDDING_DIMENSIONS
from core.enumerate import EmbeddingModel
from core.loggers.app_logging import logger
from core.utils.vectorstore_utils import load_chroma_vector_store
from langchain_openai import OpenAIEmbeddings


def create_chatbot_configs():
    # TODO:
    configs = None # noqa

    embedding_dimensions = (
        EMBEDDING_3_DIMENSIONS
        if settings.EMBEDDING_MODEL == EmbeddingModel.EMBEDDING_V3_LARGE.value
        and SHORTEN_EMBEDDING_DIMENSIONS
        else None
    )

    general_embedding_function = OpenAIEmbeddings(
        openai_api_key=settings.OPENAI_API_KEY,
        model=settings.EMBEDDING_MODEL,
        dimensions=embedding_dimensions,
    )

    logger.info(f"Using Embedding model: {settings.EMBEDDING_MODEL}")

    # TODO:
    # Language models setup
    llms = None

    # TODO:
    # Setup tools
    tools = None

    # -------- Vectorstore --------
    search_vector_store = load_chroma_vector_store(
        path=os.path.join(BASE_DIR, CHROMA_DB_PATH),
        embedding_function=general_embedding_function,
        settings=CHROMA_DEFAULT_SETTINGS,
        collection_name=EXPERTS_COLLECTION_NAME,
        tags="[Search Vectorstore]",
    )

    details_vector_store = load_chroma_vector_store(
        path=os.path.join(BASE_DIR, CHROMA_DB_DETAILS_PATH),
        embedding_function=general_embedding_function,
        settings=CHROMA_DEFAULT_SETTINGS,
        collection_name=DETAIL_EXPERTS_COLLECTION_NAME,
        tags="[Details Vectorstore]",
    )

    examples_vector_store = load_chroma_vector_store(
        path=os.path.join(BASE_DIR, CHROMA_EXAMPLES_PATH),
        embedding_function=general_embedding_function,
        settings=CHROMA_DEFAULT_SETTINGS,
        collection_name=EXAMPLES_COLLECTION_NAME,
        tags="[Examples Vectorstore]",
    )

    return (
        llms,
        tools,
        search_vector_store,
        details_vector_store,
        examples_vector_store,
        general_embedding_function,
    )
