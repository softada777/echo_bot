# handlers/start_help.py
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from lexicon.lexicon import LEXICON
from keyboards.main_menu import main_menu_kb
from database.birthday_db import birthdays
from services.birthday_service import register_user

router: Router = Router()

@router.message(F.text == "/start")
async def cmd_start(message: Message):
    await message.answer(
        LEXICON['start'],
        reply_markup=main_menu_kb  # Показываем клавиатуру
    )

@router.message(F.text == "/help")
async def cmd_help(message: Message):
    await message.answer(LEXICON['help'])