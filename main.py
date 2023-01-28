import logging
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TG_TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TG_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)


def main():
    from handlers import dp
    loop = asyncio.new_event_loop()
    loop.create_task(
        dp.start_polling(fast=True)
    )
    loop.run_forever()


if __name__ == "__main__":
    main()
