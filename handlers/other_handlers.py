from lexicon.lexicon import LEXICON_RU

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery


router: Router = Router(name=__name__)


@router.callback_query(F.data == 'cancel')
async def process_cancel_press(callback: CallbackQuery) -> None:
    await callback.message.edit_text(LEXICON_RU['cancel_text'])


@router.message()
async def process_other(message: Message):
    await message.answer(LEXICON_RU['other_text'] % message.text)