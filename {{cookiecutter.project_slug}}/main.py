import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi.exception_handlers import http_exception_handler
from langfuse.callback import CallbackHandler as LangfuseCallbackHandler
from langserve import add_routes
from starlette.middleware.cors import CORSMiddleware

from configs.common_config import settings
from configs.database import HealthcheckModel
from core.exception_handlers import chatbot_exception_error_handler
from core.exception_handlers import openai_request_error_handler
from core.exception_handlers import openai_timeout_error_handler
from core.exception_handlers import unexpected_exception_handler
from core.exceptions import ChatbotException
from core.exceptions import CustomBaseException
from core.exceptions import OpenAIException
from core.exceptions import OpenAITimeoutException
from core.helpers.vector_store_helper import chain

load_dotenv()


app = FastAPI(
    swagger_ui_parameters={"syntaxHighlight": False},
    title="{{ cookiecutter.project_slug }} API",
    description="{{ cookiecutter.short_description }} API service",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_origin_regex=settings.CORS_ORIGINS_REGEX,
    allow_credentials=True,
    allow_methods=("GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"),
    allow_headers=settings.CORS_HEADERS,
)

# Base exception handler
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(CustomBaseException, unexpected_exception_handler)

# Chatbot exception handler
app.add_exception_handler(ChatbotException, chatbot_exception_error_handler)
app.add_exception_handler(OpenAITimeoutException, openai_timeout_error_handler)
app.add_exception_handler(OpenAIException, openai_request_error_handler)


langfuse_handler = LangfuseCallbackHandler(
    public_key=os.environ["LANGFUSE_PUBLIC_KEY"],
    secret_key=os.environ["LANGFUSE_SECRET_KEY"],
    host=os.environ["LANGFUSE_HOST"],
)

# Edit this to add the chain you want to add
add_routes(app, chain, path="/chat", playground_type="chat")


@app.get(
    "/healthcheck",
    status_code=status.HTTP_200_OK,
    response_model=HealthcheckModel,
    tags=["Healthcheck"],
)
async def healthcheck() -> dict[str, str]:
    """Function checks server's health

    Returns:
        Dict: Server is running
    """
    return {"status": "ok"}
