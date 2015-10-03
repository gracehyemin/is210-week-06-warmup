#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Uses for loop."""


def process_data(data):
    """This function will output sum of the data inputs and average.

    Args:
        data(list): numbers

    Returns:
        tuple: total and average

    Examples:
        >>> process_data([1, 3, 5])
        (9, 3.0)
        >>> process_data([1, 3, 5, 7])
        (16, 4.0)

    """
    total = 0
    average = 0
    for value in data:
        total += value

    average = total/float(len(data))
    return total, average
