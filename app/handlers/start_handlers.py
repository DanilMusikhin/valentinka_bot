from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

import json
import random
import logging


"""
    Переменные и функции для работы 
"""
router = Router()
logger = logging.getLogger(__name__)
REASONS_FILE = "reasons.json"
WELCOME_MESSAGE = """Варюша, привет! 👋👋👋

К сожалению, я пока не могу подарить тебе какой-нибудь подарок в виде большого букета цветов или крупного подарка сегодня (14 февраля 2026 года). Я просто готовлюсь к твоему дню рождения и к нашей годовщине.  

Поэтому дарю тебе плоды моей учебы, моих стараний, моих знаний. Разрабатывать у меня получается неплохо. Поэтому вот тебе мой подарок.

Я тебя очень сильно люблю, ты мой ангелочек, и если ты будешь когда-нибудь сомневаться в том, люблю я тебя или нет. Обратись с этому боту.

Я тебя ОЧЕНЬ-ОЧЕНЬ СИЛЬНО-СИЛЬНО ЛЮБЛЮ, и вот почему:
"""

def load_reasons():
    with open(REASONS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

"""
    Клавиатуры
"""
def get_reason_keyboard():
    kb = InlineKeyboardBuilder()

    kb.button(
        text="💝 Причина почему я тебя люблю",
        callback_data="get_reason"
    )

    return kb.as_markup()

"""
    Хэндлеры
"""
@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        WELCOME_MESSAGE,
        reply_markup=get_reason_keyboard()
    )

@router.callback_query(F.data == "get_reason")
async def reason_callback(callback: CallbackQuery):
    reasons = load_reasons()
    reason = random.choice(reasons)

    await callback.answer()

    await callback.message.edit_text(reason, reply_markup=get_reason_keyboard())
