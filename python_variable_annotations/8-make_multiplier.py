#!/usr/bin/python3
""" complex types function """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def that_multi(x: float) -> float:
        return x * multiplier
    return that_multi
