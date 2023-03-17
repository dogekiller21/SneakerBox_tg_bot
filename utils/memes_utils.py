import logging

from asyncpraw import Reddit
from asyncprawcore import ResponseException

from config import REDDIT_CLIENT_ID, REDDIT_SECRET, REDDIT_PASSWORD, REDDIT_USERNAME


class Subreddits:
    CATS = "cats"
    MEMES = "memes"


class RedditMemeGiver:
    def __init__(self):
        self.reddit: Reddit | None = None

    async def get_random_pic_url(self, subreddit: Subreddits = Subreddits.CATS):
        if self.reddit is None:
            logging.info(f"Reddit was not initialized until now")
            self.reddit = Reddit(
                client_id=REDDIT_CLIENT_ID,
                client_secret=REDDIT_SECRET,
                user_agent="ubuntu:sneaker_bot:v0.1.2 (by /u/dogekiller21)",
                password=REDDIT_PASSWORD,
                username=REDDIT_USERNAME,
            )
        subreddit = await self.reddit.subreddit(display_name=subreddit)
        try:
            while True:
                # TODO: тут если какое-то время не трогать, начинает очень долго отвечать
                random_submission = await subreddit.random()
                pic_url = random_submission.url
                if pic_url.endswith(".jpg"):
                    return random_submission.url
        except ResponseException as e:
            logging.info(f"Response error - {e}")
            return


reddit_meme_giver = RedditMemeGiver()
