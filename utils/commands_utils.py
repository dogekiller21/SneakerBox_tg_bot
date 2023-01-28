from aiogram.types import Message, ParseMode

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
        message_text += f"\n\n*Найдены повторения \\({len(not_unique_items)}\\):*\n" f"{not_unique_items_text}"
    await message.answer(
        text=message_text,
        parse_mode=ParseMode.MARKDOWN_V2,
    )
