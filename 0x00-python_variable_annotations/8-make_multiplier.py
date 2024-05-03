#!/usr/bin/env python3
""" Returns a function that multiplies a float by the given multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that
        multiplies its argument by the given multiplier.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
