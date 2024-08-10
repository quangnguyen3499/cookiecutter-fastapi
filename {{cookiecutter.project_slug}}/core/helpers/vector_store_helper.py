import os
from string import Formatter
from typing import List, Optional

from langchain.chains.query_constructor.schema import AttributeInfo
from langchain.retrievers import SelfQueryRetriever
from langchain_community.llms import BaseLLM
from langchain_qdrant import Qdrant
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings
from langchain_core.output_parsers.string import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_openai import OpenAI, OpenAIEmbeddings
from qdrant_client import QdrantClient

from core.helpers.defaults import (
    DEFAULT_DOCUMENT_CONTENTS,
    DEFAULT_METADATA_FIELD_INFO,
    DEFAULT_COLLECTION_NAME,
    DEFAULT_DOCUMENTS,
)


class Query(BaseModel):
    __root__: str


document_template = """
PASSAGE: {page_content}
METADATA: {metadata}
"""


def combine_documents(documents: List[Document]) -> str:
    """
    Combine a list of documents into a single string that might be passed further down
    to a language model.
    :param documents: list of documents to combine
    :return:
    """
    formatter = Formatter()
    return "\n\n".join(
        formatter.format(
            document_template,
            page_content=document.page_content,
            metadata=document.metadata,
        )
        for document in documents
    )


def create_chain(
    llm: Optional[BaseLLM] = None,
    embeddings: Optional[Embeddings] = None,
    document_contents: str = DEFAULT_DOCUMENT_CONTENTS,
    metadata_field_info: List[AttributeInfo] = DEFAULT_METADATA_FIELD_INFO,
    collection_name: str = DEFAULT_COLLECTION_NAME,
):
    """
    Create a chain that can be used to query a Qdrant vector store with a self-querying
    capability. By default, this chain will use the OpenAI LLM and OpenAIEmbeddings, and
    work with the default document contents and metadata field info. You can override
    these defaults by passing in your own values.
    :param llm: an LLM to use for generating text
    :param embeddings: an Embeddings to use for generating queries
    :param document_contents: a description of the document set
    :param metadata_field_info: list of metadata attributes
    :param collection_name: name of the Qdrant collection to use
    :return:
    """
    llm = llm or OpenAI()
    embeddings = embeddings or OpenAIEmbeddings()

    # Set up a vector store to store your vectors and metadata
    client = QdrantClient(
        url=os.environ.get("QDRANT_URL", "http://localhost:6333"),
        api_key=os.environ.get("QDRANT_API_KEY"),
    )
    vectorstore = Qdrant(
        client=client,
        collection_name=collection_name,
        embeddings=embeddings,
    )

    # Set up a retriever to query your vector store with self-querying capabilities
    retriever = SelfQueryRetriever.from_llm(llm, vectorstore, document_contents, metadata_field_info, verbose=True)

    context = RunnableParallel(
        context=retriever | combine_documents,
        query=RunnablePassthrough(),
    )

    llm_context_prompt_template = """
    Answer the user query using provided passages. Each passage has metadata given as 
    a nested JSON object you can also use. When answering, cite source name of the passages 
    you are answering from below the answer in a unique bullet point list.

    If you don't know the answer, just say that you don't know, don't try to make up an answer.

    ----
    {context}
    ----
    Query: {query}
    """  # noqa: E501

    llm_context_prompt = PromptTemplate.from_template(llm_context_prompt_template)

    pipeline = context | llm_context_prompt | llm | StrOutputParser()
    return pipeline.with_types(input_type=Query)


def initialize(
    embeddings: Optional[Embeddings] = None,
    collection_name: str = DEFAULT_COLLECTION_NAME,
    documents: List[Document] = DEFAULT_DOCUMENTS,
):
    """
    Initialize a vector store with a set of documents. By default, the documents will be
    compatible with the default metadata field info. You can override these defaults by
    passing in your own values.
    :param embeddings: an Embeddings to use for generating queries
    :param collection_name: name of the Qdrant collection to use
    :param documents: a list of documents to initialize the vector store with
    :return:
    """
    embeddings = embeddings or OpenAIEmbeddings()

    # Set up a vector store to store your vectors and metadata
    Qdrant.from_documents(
        documents,
        embedding=embeddings,
        collection_name=collection_name,
        url=os.environ.get("QDRANT_URL", "http://localhost:6333"),
        api_key=os.environ.get("QDRANT_API_KEY"),
    )


# Create the default chain
chain = create_chain()
