from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ParseMode

from main import dp
from messages.basic_messages import PARSE_RE_EVAL_COMMAND_MESSAGE, REGEX_TAGS_TEXT_ERROR, LOWER_THEN_MIN_ROWS_MESSAGE, \
    PARSE_STOCK_COMMAND_MESSAGE
from states import AbibasForm
from utils.commands_utils import rows_portion_processing
from utils.tags_parsing import parse_tags_from_text, regex_upc_rows, count_parsed_tags, regex_upc_and_stock_rows


@dp.message_handler(commands=["re_evaluation"], state="*")
async def parse_re_eval_command(message: Message):
    await message.answer(
        text=PARSE_RE_EVAL_COMMAND_MESSAGE, parse_mode=ParseMode.MARKDOWN_V2
    )
    await AbibasForm.re_evaluation.set()


@dp.message_handler(commands=["stock"], state="*")
async def parse_stock_command(message: Message):
    await message.answer(
        text=PARSE_STOCK_COMMAND_MESSAGE, parse_mode=ParseMode.MARKDOWN_V2
    )
    await AbibasForm.stock.set()


@dp.message_handler(state=[AbibasForm.re_evaluation, AbibasForm.stock])
async def basic_message_handler(message: Message, state: FSMContext):
    text = message.text
    _state = await state.get_state()
    if _state == AbibasForm.re_evaluation.state:
        matched_rows = regex_upc_rows(text=text)
    else:
        matched_rows = regex_upc_and_stock_rows(text=text)
    if not matched_rows:
        await message.answer(
            text=REGEX_TAGS_TEXT_ERROR, parse_mode=ParseMode.MARKDOWN_V2
        )
        return
    if _state == AbibasForm.stock.state:
        await message.answer(
            text="\n".join(parse_tags_from_text(matched_rows)),
            parse_mode=ParseMode.MARKDOWN_V2
        )
        await state.finish()
        return
    matched_rows = sorted(matched_rows)
    remaining_rows_count = len(matched_rows)
    offset = 0
    while remaining_rows_count > 0:
        if remaining_rows_count < 32:
            count = remaining_rows_count
        else:
            count = 32
        rows_portion = matched_rows[offset:offset + count]
        await rows_portion_processing(
            rows_portion=rows_portion,
            message=message
        )
        remaining_rows_count -= 32
        offset += count

    if len(matched_rows) < 32:
        await message.answer(
            text=LOWER_THEN_MIN_ROWS_MESSAGE.format(count=len(matched_rows)),
            parse_mode=ParseMode.MARKDOWN_V2
        )
    await state.finish()


# TODO: random meme command
