import hashlib
from typing import NoReturn

from src.utils.get_info import get_info

from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.types import Message, InputTextMessageContent, InlineQueryResultArticle
from aiogram.enums import ParseMode

main_router = Router()

# NOTE (makhmud): FOR PRIVATE MESSAGES
@main_router.message(CommandStart())
async def default_handler(message: Message) -> NoReturn:
    pattern = dict(
        text=f"👋 Salom <b>{message.from_user.full_name}</b>!\n" \
             f"🌦 <b>Ob-Havo</b> botiga xush kelibsiz!\n" \
             f"🚀 Men <b>inline rejim</b>da ham ishlayman."
    )
    await message.answer(**pattern)


@main_router.message()
async def get_weather(message: Message) -> NoReturn:
    result = get_info(message.text)
    await message.reply(
        result,
        parse_mode=ParseMode.HTML
    )


# NOTE (makhmud): FOR INLINE MESSAGES
@main_router.inline_query()
async def inline_handler(inline_query: types.InlineQuery) -> NoReturn:
    result = get_info(inline_query.query or "Ma\'lumot topilmadi")
    input_content = InputTextMessageContent(
        message_text=result
    )
    result_id = hashlib.md5(result.encode()).hexdigest()
    item = InlineQueryResultArticle(
        id=result_id,
        input_message_content=input_content,
        title=(inline_query.query.title() if result != "Ma\'lumot topilmadi" else "Ma\'lumot topilmadi")
    )

    await inline_query.answer(
        results=[item],

    )
