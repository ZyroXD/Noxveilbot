import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

BOT_TOKEN =' 8811207886:AAH0TG1SoTpyi8IST6cr8qOLleQxKxD31Kc'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "🎵 Instagram Note Bot\n\n"
        "Bot is online!\n\n"
        "Commands:\n"
        "/note <text>\n"
        "/status"
    )


@dp.message(Command("note"))
async def note(message: Message):
    text = message.text.replace("/note", "", 1).strip()

    if not text:
        await message.answer("Usage:\n/note Your text")
        return

    await message.answer(f"📝 Note received:\n{text}")


@dp.message(Command("status"))
async def status(message: Message):
    await message.answer("🟢 Telegram bot is running.")


async def main():
    print("Bot started...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

