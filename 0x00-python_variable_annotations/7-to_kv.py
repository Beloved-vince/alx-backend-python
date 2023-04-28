"""
    Three data type to tuple
"""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    returns tuple taking k and v as args
    """

    return (k, v**2)