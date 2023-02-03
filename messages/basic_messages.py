PARSE_RE_EVAL_COMMAND_MESSAGE = (
    "*Введите текст с почты*\n\n"
    "*Формат:*\n"
    "```\n"
    "[UPC-EAN]: 1234567890123\n"
    "[UPC-EAN]: 1234567890123\n"
    "[UPC-EAN]: 1234567890123\n"
    "..."
    "```"
)

PARSE_STOCK_COMMAND_MESSAGE = (
    "*Введите текст с почты*\n\n"
    "*Формат:*\n"
    "```\n"
    "[UPC-EAN]: 1234567890123\n"
    "[UPC-EAN]: 1234567890123\n"
    "[C128]: 1234567890\n"
    "..."
    "```"
)

REGEX_TAGS_TEXT_ERROR = "Ни одна из строк текста не подходит"


# Message with formatting
LOWER_THEN_MIN_ROWS_MESSAGE = (
    "*Вы отправили меньше 32 позиций*\n"
    "_Всего отправлено: *{count}*_"
)
