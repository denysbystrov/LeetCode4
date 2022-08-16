"""Number 412: Fizz Buzz"""
from typing import List


def fizz_buzz(n: int) -> List[str]:
    r = []
    for i in range(1, n+1):
        s = 'Fizz' if i % 3 == 0 else ''
        s += 'Buzz' if i % 5 == 0 else ''
        r.append(s) if s else r.append(str(i))

    return r
