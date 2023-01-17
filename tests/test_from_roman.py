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
