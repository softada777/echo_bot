from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def send_user_id(message: Message) -> None:
    user_id = message.from_user.id
    print("ID пользователя:", user_id)
    await message.answer(f"Ваш Telegram ID: {user_id}")

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет! Я Эхо-бот. Отправь мне текст или фото.")

@dp.message(Command("help"))
async def help(message: Message):
    await message.answer("Просто напиши мне что-нибудь, и я отвечу тем же.")

@dp.message(Command("caps"))
async def caps(message: Message):
    text = message.text[6:]
    await message.reply(text.upper())

@dp.message(Command("reverse"))
async def reverse(message: Message):
    text = message.text[9:]
    await message.reply(text[::-1])

@dp.message(F.text.lower().in_(["адиля дура", "маты", "аморальщина"]))
async def handle_ban(message: Message):
    await message.reply("Не говори такие плохие слова!! это не культурно((")

@dp.message(F.photo)
async def handle_photo(message: Message):
    caption = message.caption or "Дефолт фото"
    await message.reply(f"Вы отправили фото: {caption}")

@dp.message(F.text)
async def handle_text(message: Message):
    await message.reply(message.text)

@dp.message(F.voice)
async def handle_voice(message: Message):
    await message.reply("Это голосовуха, я не могу послушать(((")

@dp.message(F.animation)
async def handle_gif(message: Message):
    await message.reply("ВАУ четкая гифка!!!!!!")

@dp.message(F.sticker)
async def handle_sticker(message: Message):
    await message.reply("Адиль, стикер милый, но давай лучше поговорим :)")

if __name__ == '__main__':
    dp.run_polling(bot)