#!/usr/bin/env python3
"""Augment the following code with the correct duck-typed annotations:"""
import typing


def safe_first_element(
        lst: typing.Sequence[typing.Any]) -> typing.Union[typing.Any, None]:
    if lst:
        return lst[0]
    else:
        return None
