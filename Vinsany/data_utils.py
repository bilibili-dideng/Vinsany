"""
Data processing utilities for calculating basic statistics.
This module provides functions for:
- Calculating mean
- Calculating median
- Returning min and max values
- Calculating standard deviation
- Summing values
- Analyzing data (find max, min, repeated values)
"""

from typing import List, Union, Dict
from collections import Counter


def mean(data: List[Union[int, float]]) -> float:
    """
    Calculate the average (mean) of a list of numbers.

    :param data: List of numerical values
    :return: Mean value
    :raises ValueError: If the input list is empty
    """
    if not data:
        raise ValueError("Input data cannot be empty")
    return sum(data) / len(data)


def median(data: List[Union[int, float]]) -> Union[int, float]:
    """
    Calculate the median of a list of numbers.

    :param data: List of numerical values
    :return: Median value
    :raises ValueError: If the input list is empty
    """
    if not data:
        raise ValueError("Input data cannot be empty")
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]


def max_value(data: List[Union[int, float]]) -> Union[int, float]:
    """
    Return the maximum value in the list.

    :param data: List of numerical values
    :return: Maximum value
    """
    return max(data)


def min_value(data: List[Union[int, float]]) -> Union[int, float]:
    """
    Return the minimum value in the list.

    :param data: List of numerical values
    :return: Minimum value
    """
    return min(data)


def std_dev(data: List[Union[int, float]]) -> float:
    """
    Calculate the standard deviation of a list of numbers.

    :param data: List of numerical values
    :return: Standard deviation
    :raises ValueError: If the input list is empty
    """
    if not data:
        raise ValueError("Input data cannot be empty")
    avg = mean(data)
    variance = sum((x - avg) ** 2 for x in data) / len(data)
    return variance ** 0.5


def total_sum(data: List[Union[int, float]]) -> Union[int, float]:
    """
    Return the total sum of all values in the list.

    :param data: List of numerical values
    :return: Total sum
    """
    return sum(data)


def analyze_data(*data: Union[int, float]) -> Dict[str, Union[int, float, Dict[Union[int, float], int]]]:
    """
    Analyze the input data to find:
    - Maximum value
    - Minimum value
    - Repeated values (and their counts)

    :param data: Variable-length list of numerical values
    :return: Dictionary containing analysis results
    :raises ValueError: If no data is provided
    """
    if not data:
        raise ValueError("No data provided for analysis")

    max_val = max(data)
    min_val = min(data)
    counts = Counter(data)
    repeated = {value: count for value, count in counts.items() if count > 1}

    return {
        "max": max_val,
        "min": min_val,
        "repeated": repeated
    }