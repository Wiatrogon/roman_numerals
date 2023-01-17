import re


def is_valid(number: str) -> bool:
    pattern = re.compile(r"[MDCLXVI]+")

    return bool(pattern.match(number))
