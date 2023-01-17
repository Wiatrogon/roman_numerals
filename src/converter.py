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
    # strip thousands
    thousands = 0
    while number.startswith("M"):
        thousands += 1000
        number = number[1:]

    # strip hundreds
    hundreds = 0
    if number.startswith("CM"):
        hundreds += 900
        number = number[2:]
    elif number.startswith("CD"):
        hundreds += 400
        number = number[2:]
    elif number.startswith("D"):
        hundreds += 500
        number = number[1:]

    while number.startswith("C"):
        hundreds += 100
        number = number[1:]

    # strip tens
    tens = 0
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

    return thousands + hundreds + tens + ones
