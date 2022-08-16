import pytest
from interview2 import tree_of_errors


test_cases = (
    ('    (A,B)', 'E1'),
    ('(A,B)  (A,C)', 'E1'),
    ('(A, B) (D,C)', 'E1'),
    ('(A,B),(D,C)', 'E1'),
    ('(A,B) (B,D) (A,C)   ', 'E1'),
    ('(a,B) (B,C)', 'E1'),
    ('(AB,B) (D,C)', 'E1'),
    ('(A,B) {B,C} (A,D)', 'E1'),
    ('(A,B) (B,C) (A, D) \n(C, E)', 'E1'),
    ('(A,B) (B,C) (A,B)', 'E2'),
    ('(A,B) (A,C) (B,D) (A,E)', 'E3'),
    ('(A,B) (A,C) (B,D) (E,F)', 'E4'),
    ('(A,B) (B,C) (C,A)', 'E5'),
    ('(A,B) (B,C) (C,A) (A,B)', 'E2'),
    ('(A,B) (A,C) (B,D) (A,E)  ', 'E1'),
)


@pytest.mark.parametrize(('inp', 'expected'), test_cases)
def test_tree_of_errors(inp, expected):
    assert tree_of_errors(inp) == expected
