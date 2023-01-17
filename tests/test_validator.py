import pytest

from src.validator import is_valid


@pytest.mark.parametrize("number", ["I", "V", "X", "L", "C", "D", "M"])
def test_single_character_valid_roman_numeral(number):
    assert is_valid(number) is True


@pytest.mark.parametrize("number", ["IV", "VI", "IX", "XI", "XL", "LI", "LV", "LX", "XC", "CI", "CV", "CD", "CM"])
def test_two_characters_valid_roman_numerals(number):
    assert is_valid(number) is True
