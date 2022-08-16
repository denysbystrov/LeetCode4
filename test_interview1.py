import pytest
from interview1 import days_between


test_cases = (
    (2004, 5, 10, 2004, 5, 11, 1),
    (2018, 1, 13, 2018, 7, 5, 173),
    (2020, 1, 13, 2020, 7, 5, 174),
    (2010, 2, 13, 2011, 2, 13, 365),
    (2010, 10, 24, 2011, 1, 17, 85),
    (2002, 8, 10, 2007, 3, 3, 1666)
)


@pytest.mark.parametrize(('year1', 'month1', 'day1', 'year2', 'month2', 'day2', 'expected'), test_cases)
def test_days_between(year1, month1, day1, year2, month2, day2, expected):
    assert days_between(year1, month1, day1, year2, month2, day2) == expected
