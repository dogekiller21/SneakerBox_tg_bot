from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ParseMode

from main import dp
from messages.basic_messages import PARSE_TAGS_COMMAND_MESSAGE, REGEX_TAGS_TEXT_ERROR
from states import AbibasForm
from utils.tags_parsing import parse_tags_from_text, regex_rows, count_parsed_tags


@dp.message_handler(commands=["parse_tags"], state="*")
async def parse_tags_command(message: Message):
    await message.answer(
        text=PARSE_TAGS_COMMAND_MESSAGE,
        parse_mode=ParseMode.MARKDOWN_V2
    )
    await AbibasForm.rows.set()


@dp.message_handler(state=AbibasForm.rows)
async def basic_message_handler(message: Message, state: FSMContext):
    text = message.text
    matched_rows = regex_rows(text)
    if not matched_rows:
        await message.answer(
            text=REGEX_TAGS_TEXT_ERROR,
            parse_mode=ParseMode.MARKDOWN_V2
        )
        return
    parsed_items = parse_tags_from_text(matched_rows)
    unique_items = sorted(list(set(parsed_items)))
    not_unique_items: dict[str, int] = count_parsed_tags(parsed_tags=parsed_items)
    await message.answer(
        text="\n".join(map(str, unique_items)),
    )
    if not_unique_items:
        sorted_not_unique_items = list(map(lambda x: (str(x[0]), x[1]), sorted(
            not_unique_items.items(),
            key=lambda x: x[0]
        )))
        not_unique_items_text = "\n".join(
            f"{tag[-4:]}: {count}" for tag, count in sorted_not_unique_items
        )
        await message.answer(
            text=f"*Найдены повторения:*\n"
                 f"{not_unique_items_text}",
            parse_mode=ParseMode.MARKDOWN_V2
        )
    await state.finish()
