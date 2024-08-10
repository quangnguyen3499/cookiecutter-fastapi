from fastapi import APIRouter

from app.chat.router import chat_router

router = APIRouter(prefix="/api")
router.include_router(chat_router)
