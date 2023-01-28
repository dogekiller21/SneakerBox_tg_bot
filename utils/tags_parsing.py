import re
from collections import Counter


def regex_rows(text: str) -> list[str]:
    pattern = re.compile(r"\[UPC-EAN]: \d{13}")
    return re.findall(pattern, text)


def parse_tags_from_text(rows: list[str]) -> list[int]:
    """
    list ["text1_0: text2_0", "text1_1: text2_1", ...] -> list ["text2_0", "text2_1", ...]
    :param rows: list[str]
    :return: list[str]
    """
    return list(map(int, (row.split(":")[1].strip() for row in rows)))


def count_parsed_tags(parsed_tags: list[int]) -> dict[str, int]:
    return {tag: count for tag, count in Counter(parsed_tags).items() if count > 1}
