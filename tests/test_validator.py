import pytest

from src.validator import is_valid


@pytest.mark.parametrize("number", ["FOO", "BAR"])
def test_invalid_characters(number):
    assert is_valid(number) is False


@pytest.mark.parametrize("number", ["I", "V", "X", "L", "C", "D", "M"])
def test_single_character_valid_roman_numeral(number):
    assert is_valid(number) is True


@pytest.mark.parametrize("number", ["IV", "IX", "VI", "XI", "XV", "XL", "XC",
                                    "LI", "LV", "LX", "CI", "CV", "CL", "CD",
                                    "CM", "DI", "DV", "DX", "DL", "DC", "MI",
                                    "MV", "MX", "ML", "MC", "MD", "MM"])
def test_two_characters_valid_roman_numerals(number):
    assert is_valid(number) is True


@pytest.mark.parametrize("number", ["IL", "IC", "ID", "IM", "VX", "VL", "VC",
                                    "VD", "VM", "XD", "XM", "LC", "LD", "LM", "DM"])
def test_two_characters_invalid_roman_numerals(number):
    assert is_valid(number) is False


@pytest.mark.parametrize("number", ["III", "VII", "XII", "XIV", "XVI", "XIX",
                                    "XXI", "XXV", "XXX", "XLI", "XLV", "LII",
                                    "LIV", "LVI", "LIX", "LXI", "XCI", "XCV",
                                    "CII", "CIV", "CVI", "CIX", "CXI", "CXV",
                                    "CXL", "CLI", "CLV", "CLX", "CXC", "CCI",
                                    "CCV", "CCX", "CCL", "CCC", "CDI", "CDV",
                                    "CDX", "CDL", "DII", "DIV", "DVI", "DIX",
                                    "DXI", "DXL", "DLI", "DLV", "DLX", "DXC",
                                    "DCI", "DCV", "DCX", "DCL", "CMI", "CMV",
                                    "CMX", "CML", "MMI", "MMV", "MMX", "MML",
                                    "MMC", "MMD", "MMM"])
def test_three_characters_valid_roman_numerals(number):
    assert is_valid(number) is True


@pytest.mark.parametrize("number", ["IIV", "IIX", "IIL", "IIC", "IID", "IIM",
                                    "IVI", "IXI", "ILI", "ICI", "IDI", "IMI",
                                    "VVI", "LLI", "LLX", "DDI", "DDX", "DDC"])
def test_three_characters_invalid_roman_numerals(number):
    assert is_valid(number) is False