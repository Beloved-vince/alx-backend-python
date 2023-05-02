#!/usr/bin/env python3
""" The basics of async """

from asyncio import run
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ From the previous file, import wait_n into 2-measure_runtime.py.
        Create a measure_time function with integers n and max_delay as arguments
        that measures the total execution time for wait_n(n, max_delay), and returns total_time / n. 
        the function should return a float.
        Use the time module to measure an approximate elapsed time.
    """
    start = time()

    run(wait_n(n, max_delay))

    end = time()

    return (end - start) / n