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
    return _ones.index(number)
