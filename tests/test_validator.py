import pytest

from src.validator import is_valid


@pytest.mark.parametrize("number", ["FOO", "BAR"])
def test_invalid_characters(number):
    assert is_valid(number) is False


@pytest.mark.parametrize("number", ["I", "V", "X", "L", "C", "D", "M"])
def test_single_character_valid_roman_numeral(number):
    assert is_valid(number) is True


@pytest.mark.parametrize("number", ["IV", "VI", "IX", "XI", "XL", "LI", "LV",
                                    "LX", "XC", "CI", "CV", "CD", "CM"])
def test_two_characters_valid_roman_numerals(number):
    assert is_valid(number) is True


@pytest.mark.parametrize("number", ["IL", "IC", "ID", "IM", "VX", "VL", "VC",
                                    "VD", "VM", "XD", "XM", "LC", "LD", "LM", "DM"])
def test_two_characters_invalid_roman_numerals(number):
    assert is_valid(number) is False
