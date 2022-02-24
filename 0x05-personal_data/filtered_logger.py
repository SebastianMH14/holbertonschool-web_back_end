#!/usr/bin/env python3
"""function called filter_datum
that returns the log message obfuscated"""
from typing import List
import re


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str) -> str:
    """ use a regex to replace occurrences of certain"""
    for field in fields:
        message = re.sub(r'({}=).*?{}'.format(field, separator),
                         r'\1{}{}'.format(redaction, separator), message)
    return message
