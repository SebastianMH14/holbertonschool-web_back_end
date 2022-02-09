#!/usr/bin/env python3
"""Implement a method named get_page that takes
two integer arguments page with default value 1
and page_size with default value 10."""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ function should return a tuple of size two containing
    a start index and an end index corresponding to the range
    of indexes to return in a list for those particular
    pagination parameters."""
    pages = page * page_size
    size = pages - page_size
    return (size, pages)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert (type(page) == int)
        assert (page > 0)
        assert (type(page_size) == int)
        assert (page_size > 0)
        index = index_range(page, page_size)
        pages = self.dataset()
        if (index[0] > len(pages)):
            return []
        return pages[index[0]:index[1]]
