from src.converter import to_roman


def test_single_digit_solutions():
    assert to_roman(1) == "I"
    assert to_roman(5) == "V"
    assert to_roman(10) == "X"
    assert to_roman(50) == "L"
    assert to_roman(100) == "C"
    assert to_roman(1000) == "M"


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
    assert to_roman(101) == "CI"
    assert to_roman(105) == "CV"
    assert to_roman(110) == "CX"
    assert to_roman(150) == "CL"
    assert to_roman(200) == "CC"
    assert to_roman(400) == "CD"
    assert to_roman(600) == "DC"
    assert to_roman(900) == "CM"
    assert to_roman(1001) == "MI"
    assert to_roman(1010) == "MX"
    assert to_roman(2000) == "MM"


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
    assert to_roman(111) == "CXI"
    assert to_roman(222) == "CCXXII"
    assert to_roman(444) == "CDXLIV"
    assert to_roman(666) == "DCLXVI"
    assert to_roman(888) == "DCCCLXXXVIII"
    assert to_roman(999) == "CMXCIX"
    assert to_roman(1337) == "MCCCXXXVII"
    assert to_roman(2077) == "MMLXXVII"
