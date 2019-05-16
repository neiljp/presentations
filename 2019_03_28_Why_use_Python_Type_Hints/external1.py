from typing import List
import math

def func(x: List[int]) -> int:
    return sum(x)

func([])
func(range(4))
func(list(range(4)))
func(set(range(4)))
func([1, 'a'])

func([3,4]).join([5,6])
func([4,4])+1
math.sqrt(func([9,3]))
