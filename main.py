import logging
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import Message, ParseMode
from config import TG_TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TG_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)


def parse_text(text: str) -> list[str]:
    rows = list(map(int, (row.split(":")[1] for row in text.split("\n"))))
    return list(map(str, sorted(rows)))


@dp.message_handler()
async def basic_message_handler(message: Message):
    text = message.text
    try:
        parsed_items = parse_text(text)
    except Exception as _:
        await message.answer(
            text="*\\[\\!\\]* Ошибочка\n"
                 "__Возможно данные введены неверно__",
            parse_mode=ParseMode.MARKDOWN_V2
        )
        return
    await message.answer(
        text="\n".join(parsed_items)
    )


def main():
    loop = asyncio.new_event_loop()
    loop.create_task(
        dp.start_polling(fast=True)
    )
    loop.run_forever()


if __name__ == "__main__":
    main()
