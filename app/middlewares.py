""" | Файл для мидварей | """

from aiogram import types
from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject
from typing import Any, Callable, Dict, Awaitable

from config.config_reader import config


class LoversCheckMiddleWare(BaseMiddleware):
    async def __call__(
        self, 
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]], 
        event: TelegramObject,
        data: dict[str, Any]
    ) -> Any:
        user_id = event.from_user.id

        if user_id not in [config.my_id, config.varya_id]:
            return # Прерываем работу

        return await handler(event, data)