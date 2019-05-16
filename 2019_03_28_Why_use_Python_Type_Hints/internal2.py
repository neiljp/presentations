from typing import Iterable
import math

def good(x: Iterable[int]) -> int:
    return sum(math.sqrt(element) for element in x)
