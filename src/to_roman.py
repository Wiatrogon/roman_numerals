def to_roman(number: int) -> str:
    ones = number % 10
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"][ones]

    tens = (number % 100) // 10
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"][tens]

    hundreds = (number % 1000) // 100
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"][hundreds]

    return f"{hundreds}{tens}{ones}"
