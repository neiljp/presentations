import typing
def annotated_func(x: int, b: str) -> None:
    pass

print(typing.get_type_hints(annotated_func))
