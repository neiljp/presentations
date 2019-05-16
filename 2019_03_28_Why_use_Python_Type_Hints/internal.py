from typing import Iterable

def good(x: Iterable[int]) -> int:
    return sum(x)

def bad(x: Iterable[int]) -> int:
    ret = ", ".join(x)
    return ret
