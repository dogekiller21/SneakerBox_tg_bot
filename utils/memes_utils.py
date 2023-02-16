import asyncio

import asyncpraw

from config import REDDIT_CLIENT_ID, REDDIT_SECRET


async def get_random_pic_url(subreddit: str = "cats"):
    async with asyncpraw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_SECRET,
        user_agent="ubuntu:sneaker_bot:v0.1.1 (by /u/dogekiller21)",
    ) as reddit:
        subreddit = await reddit.subreddit(display_name=subreddit)
        while True:
            random_submission = await subreddit.random()
            pic_url = random_submission.url
            if pic_url.endswith(".jpg"):
                return random_submission.url
