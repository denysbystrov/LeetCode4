import pytest
from longest_palindrome import longest_palindrome
from Util import is_palindrome


test_cases = (
    ('babad', 3),
    ('a', 1),
    ('abc', 1),
    ('racecar', 7),
    ('fsafabccba', 6),
    ('abbbba', 6)
)


@pytest.mark.parametrize(('input_x', 'expected_l'), test_cases)
def test_longest_palindrome(input_x, expected_l):
    r_palindrome = longest_palindrome(input_x)
    assert len(r_palindrome) == expected_l and is_palindrome(r_palindrome)
