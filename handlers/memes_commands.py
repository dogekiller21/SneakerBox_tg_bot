from aiogram.types import Message

from main import dp
from utils.commands_utils import send_random_pic
from utils.memes_utils import Subreddits


@dp.message_handler(commands="random_cat")
async def random_cat_command(message: Message):
    await send_random_pic(message=message, subreddit=Subreddits.CATS)


@dp.message_handler(commands="random_meme")
async def random_meme_command(message: Message):
    await send_random_pic(message=message, subreddit=Subreddits.MEMES)
