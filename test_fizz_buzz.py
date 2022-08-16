import pytest
from fizz_buzz import fizz_buzz


test_cases = (
    (1, ['1']),
    (15, ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"])
)


@pytest.mark.parametrize(('n', 'expected'), test_cases)
def test_fizz_buzz(n, expected):
    assert fizz_buzz(n) == expected
