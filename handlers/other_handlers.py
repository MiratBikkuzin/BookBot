from lexicon.lexicon import LEXICON_RU

from aiogram import Router
from aiogram.types import Message


router: Router = Router(name='OtherRouter')


@router.message()
async def process_other(message: Message):
    await message.answer(LEXICON_RU['other_text'] % message.text)