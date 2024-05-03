#!/usr/bin/env python3

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the string k as the first element and the square of the int/float v as the second element.

    Args:
        k (str): The string element.
        v (Union[int, float]): The integer or float element.

    Returns:
        Tuple[str, float]: A tuple containing string k and the square of int/float v as a float.
    """
    return (k, v * v)
