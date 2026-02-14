""" | Файл настроки бота | """

# Библиотеки
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

import logging
import asyncio

# Конфиг
from app.middlewares import LoversCheckMiddleWare
from config.config_reader import config
# Обработчики
from app.handlers import start_handlers

logger = logging.getLogger(__name__)

async def main():
    # Настройка логирования
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    )
    logger.info("Логирование настроено")

    # Инициализация бота
    bot = Bot(token=config.bot_token.get_secret_value(), default=DefaultBotProperties(parse_mode= ParseMode.MARKDOWN))
    dp = Dispatcher(storage= MemoryStorage())

    # Установка команд
    commands = [
        types.BotCommand(command="/start", description="Запустить бота"),
    ]
    await bot.set_my_commands(commands)

    # Включение обработчиков и мидварей
    dp.message.middleware(LoversCheckMiddleWare())
    dp.callback_query.middleware(LoversCheckMiddleWare())
    dp.include_routers(
        start_handlers.router,
    )

    # Начало работы бота
    logger.info("Бот запущен")
    await dp.start_polling(bot, allowed_updates=["message", "inline_query", "chat_member", "my_chat_member", "callback_query"])

if __name__ == "__main__":
    asyncio.run(main())