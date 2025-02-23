"""
Module for NumPy array operations and performance testing.

This module provides utility functions for array operations
and performance comparisons with other data structures.
"""

import numpy as np
from typing import Union, List

def create_array(size: int) -> np.ndarray:
    """
    Create a NumPy array of specified size.

    Args:
        size (int): Size of the array to create.

    Returns:
        np.ndarray: Created array with values [0, 1, ..., size-1].

    Raises:
        ValueError: If size is negative.
    """
    if size < 0:
        raise ValueError("Size cannot be negative")
    return np.arange(size)

def traverse_and_sum_array(arr: Union[np.ndarray, List[int]]) -> int:
    """
    Traverse the array and sum all values.

    Args:
        arr (Union[np.ndarray, List[int]]): Input array.

    Returns:
        int: Sum of all values in the array.
    """
    return arr.sum() if isinstance(arr, np.ndarray) else sum(arr) 