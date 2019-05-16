from typing import List
def some_function(x: List[int]) -> int:
    return [greeting + " Portland!" for greeting in x]

print(some_function(['Hello', 'Hi', 'Yo']))
