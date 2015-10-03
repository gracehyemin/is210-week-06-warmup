#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""String and tuple have mutability differences."""


def flip_keys(to_flip):
    """This function will reverse the inner sequence(nested list).

    Args:
        to_flip(list): it is nested in the input

    Returns:
        list: reverse of original nested list

    Examples:
        >>>flip_keys([(1, 2, 3),'a, b, c'])
        [(3, 2, 1),'c ,b ,a']
        >>>flip_keys([(4, 6, 8),'banana'])
        [(8, 6, 4), 'ananab']

    """
    counter = 0
    for value in to_flip:
        to_flip[counter] = value[::-1]
        counter += 1
    return to_flip
