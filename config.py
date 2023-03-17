from dotenv import load_dotenv

import os

load_dotenv()

TG_TOKEN = os.getenv("TG_TOKEN")

REDDIT_SECRET = os.getenv("REDDIT_SECRET")
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_USERNAME = os.getenv("REDDIT_USERNAME")
REDDIT_PASSWORD = os.getenv("REDDIT_PASSWORD")
