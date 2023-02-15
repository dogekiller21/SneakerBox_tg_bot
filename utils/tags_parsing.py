import re
from collections import Counter


def regex_upc_rows(text: str) -> list[str]:
    pattern = re.compile(r"\[UPC-EAN]: \d+")
    return re.findall(pattern, text)


def regex_upc_and_stock_rows(text: str) -> list[str]:
    pattern = re.compile(r"\[UPC-EAN]: \d+|\[C128]: \d+")
    return re.findall(pattern, text)


def parse_tags_from_text(rows: list[str]) -> list[str]:
    """
    list ["text1_0: text2_0", "text1_1: text2_1", ...] -> list ["text2_0", "text2_1", ...]
    :param rows: list[str]
    :return: list[str]
    """
    return [
        f"*{value[1]}*" if value[0] == "[C128]" else value[1]
        for value in (list(map(lambda x: str(x).strip(), row.split(":"))) for row in rows)
    ]


def count_parsed_tags(parsed_tags: list[str]) -> dict[str, int]:
    return {tag: count for tag, count in Counter(parsed_tags).items() if count > 1}
