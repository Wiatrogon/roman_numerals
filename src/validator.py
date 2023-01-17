import re


def is_valid(number: str) -> bool:
    pattern = re.compile(r"^(C[MD]|M*D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$")

    return bool(pattern.match(number))
