#!/usr/bin/env python3

"""
more list mixed
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
        return float as sum. 
    """
    return float(sum(mxd_lst))