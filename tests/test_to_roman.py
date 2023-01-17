from src.to_roman import to_roman


def test_single_digit_solutions():
    assert to_roman(1) == "I"
    assert to_roman(5) == "V"
    assert to_roman(10) == "X"
    assert to_roman(50) == "L"


def test_two_digit_solutions():
    assert to_roman(2) == "II"
    assert to_roman(4) == "IV"
    assert to_roman(6) == "VI"
    assert to_roman(9) == "IX"
    assert to_roman(11) == "XI"
    assert to_roman(40) == "XL"
    assert to_roman(55) == "LV"
    assert to_roman(60) == "LX"
    assert to_roman(90) == "XC"


def test_multiple_digit_solutions():
    assert to_roman(3) == "III"
    assert to_roman(7) == "VII"
    assert to_roman(8) == "VIII"
    assert to_roman(22) == "XXII"
    assert to_roman(33) == "XXXIII"
    assert to_roman(44) == "XLIV"
    assert to_roman(66) == "LXVI"
    assert to_roman(77) == "LXXVII"
    assert to_roman(88) == "LXXXVIII"
    assert to_roman(99) == "XCIX"
