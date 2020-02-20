from __future__ import annotations
from typing import Any

class Element:
    def __init__(self, value: Any):
        self.value = value

    @classmethod
    def create(cls, value)->Element:

        return Element(value)

    def __str__(self) -> str:
        return f"value:{self.value}"


if __name__ == "__main__":
    ele = Element.create(123)
    print(ele)
