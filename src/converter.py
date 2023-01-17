_ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
_tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
_hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]


def to_roman(number: int) -> str:
    ones = number % 10
    ones = _ones[ones]

    tens = (number % 100) // 10
    tens = _tens[tens]

    hundreds = (number % 1000) // 100
    hundreds = _hundreds[hundreds]

    thousands = "M" * (number // 1000)

    return f"{thousands}{hundreds}{tens}{ones}"


def from_roman(number: str) -> int:
    tens = 0

    # strip tens
    if number.startswith("XC"):
        tens += 90
        number = number[2:]
    elif number.startswith("XL"):
        tens += 40
        number = number[2:]
    elif number.startswith("L"):
        tens += 50
        number = number[1:]

    while number.startswith("X"):
        tens += 10
        number = number[1:]

    ones = _ones.index(number)

    return tens + ones
