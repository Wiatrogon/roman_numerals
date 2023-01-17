from src.converter import from_roman


def test_single_digit_solutions():
    assert from_roman("IX") == 9
    assert from_roman("VIII") == 8
    assert from_roman("VII") == 7
    assert from_roman("VI") == 6
    assert from_roman("V") == 5
    assert from_roman("IV") == 4
    assert from_roman("III") == 3
    assert from_roman("II") == 2
    assert from_roman("I") == 1


def test_two_digit_solutions():
    assert from_roman("X") == 10
    assert from_roman("XI") == 11
    assert from_roman("XXII") == 22
    assert from_roman("XXX") == 30
    assert from_roman("XXXIII") == 33
    assert from_roman("XL") == 40
    assert from_roman("XLIV") == 44
    assert from_roman("L") == 50
    assert from_roman("LX") == 60
    assert from_roman("LXVI") == 66
    assert from_roman("LXXVII") == 77
    assert from_roman("LXXXVIII") == 88
    assert from_roman("XC") == 90
    assert from_roman("XCIX") == 99


def test_three_digit_solutions():
    assert from_roman("C") == 100
    assert from_roman("CI") == 101
    assert from_roman("CX") == 110
    assert from_roman("CXI") == 111
    assert from_roman("CC") == 200
    assert from_roman("CCXXII") == 222
    assert from_roman("CCC") == 300
    assert from_roman("CCCXXXIII") == 333
    assert from_roman("CD") == 400
    assert from_roman("CDXLIV") == 444
    assert from_roman("D") == 500
    assert from_roman("DLV") == 555
    assert from_roman("DC") == 600
    assert from_roman("DCLXVI") == 666
    assert from_roman("DCCLXXVII") == 777
    assert from_roman("DCCCLXXXVIII") == 888
    assert from_roman("CM") == 900
    assert from_roman("CMXCIX") == 999
