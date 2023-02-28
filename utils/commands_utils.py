from aiogram.types import Message, ParseMode, ChatActions

from utils.memes_utils import reddit_meme_giver, Subreddits
from utils.tags_parsing import parse_tags_from_text, count_parsed_tags


async def rows_portion_processing(rows_portion: list[str], message: Message):
    parsed_items = parse_tags_from_text(rows_portion)
    unique_items = sorted(list(set(parsed_items)))
    message_text = "\n".join(map(str, unique_items))
    not_unique_items: dict[str, int] = count_parsed_tags(parsed_tags=parsed_items)
    if not_unique_items:

        not_unique_items_text = "\n".join(
            f"  *\\- {tag[-4:]}: _{count}_*" for tag, count in not_unique_items.items()
        )
        message_text += (
            f"\n\n*Найдены повторения \\({len(not_unique_items)}\\):*\n"
            f"{not_unique_items_text}"
        )
    await message.answer(
        text=message_text,
        parse_mode=ParseMode.MARKDOWN_V2,
    )


async def send_random_pic(message: Message, subreddit: str = Subreddits.CATS):
    await ChatActions.upload_photo()
    random_pic_url = await reddit_meme_giver.get_random_pic_url(subreddit=subreddit)
    if random_pic_url is None:
        await message.answer(text="Произошла ошибка, попробуйте позже :(")
        return
    await message.answer_photo(photo=random_pic_url)
