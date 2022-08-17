"""Number 412: Fizz Buzz"""
from typing import List


def fizz_buzz(n: int) -> List[str]:
    r = []
    for i in range(1, n+1):
        r.append('Fizz'*(i % 3 < 1)+'Buzz'*(i % 5 < 1) or str(i))

    return r
