from aiogram.types import Message

from main import dp
from utils.commands_utils import send_random_pic
from utils.memes_utils import Subreddits


async def reddit_throttle(message: Message, *args, **kwargs):
    await message.answer("Не спамь командами!")


@dp.message_handler(commands="random_cat")
@dp.throttled(reddit_throttle, rate=2)
async def random_cat_command(message: Message):
    await send_random_pic(message=message, subreddit=Subreddits.CATS)


@dp.message_handler(commands="random_meme")
@dp.throttled(reddit_throttle, rate=2)
async def random_meme_command(message: Message):
    await send_random_pic(message=message, subreddit=Subreddits.MEMES)
