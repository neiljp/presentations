from typing import List, Optional
import math

def func(x: List[int]) -> Optional[int]:
    if x:
        return sum(x)
    return None

func([])  # Now returns None
#func(range(4))
func(list(range(4)))
#func(set(range(4)))
#func([1, 'a'])

#func([3,4]).join([5,6])
func([4,4])+1           # Type Error
math.sqrt(func([9,3]))  # Type Error
